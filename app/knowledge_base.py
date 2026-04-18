"""
Knowledge base: loads wiki markdown files and retrieves the most relevant
articles for a given query using TF-IDF–style keyword matching.
No external embedding service is required; this keeps the setup self-contained.
"""
from __future__ import annotations

import math
import os
import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class Article:
    filename: str
    title: str
    content: str
    tokens: List[str] = field(default_factory=list)


class KnowledgeBase:
    def __init__(self, wiki_dir: str, top_k: int = 3):
        self.wiki_dir = wiki_dir
        self.top_k = top_k
        self.articles: List[Article] = []
        self._idf: dict[str, float] = {}

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------

    def load(self) -> None:
        """Load all markdown files from the wiki directory."""
        if not os.path.isdir(self.wiki_dir):
            raise FileNotFoundError(f"Wiki directory not found: {self.wiki_dir}")

        files = sorted(
            f for f in os.listdir(self.wiki_dir) if f.endswith(".md")
        )
        self.articles = []
        for filename in files:
            path = os.path.join(self.wiki_dir, filename)
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
            title = self._extract_title(content, filename)
            tokens = self._tokenise(content)
            self.articles.append(Article(filename=filename, title=title, content=content, tokens=tokens))

        self._compute_idf()

    # ------------------------------------------------------------------
    # Retrieval
    # ------------------------------------------------------------------

    def retrieve(self, query: str, top_k: int | None = None) -> List[Article]:
        """Return the top-k most relevant articles for the query."""
        if not self.articles:
            return []
        k = top_k if top_k is not None else self.top_k
        q_tokens = self._tokenise(query)
        scores = [(self._score(q_tokens, article), article) for article in self.articles]
        scores.sort(key=lambda x: x[0], reverse=True)
        return [article for _, article in scores[:k]]

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_title(content: str, fallback: str) -> str:
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
        return fallback

    @staticmethod
    def _tokenise(text: str) -> List[str]:
        text = text.lower()
        # keep alphanumeric words and strip punctuation
        return re.findall(r"[a-z0-9]+", text)

    def _compute_idf(self) -> None:
        n = len(self.articles)
        df: dict[str, int] = {}
        for article in self.articles:
            for token in set(article.tokens):
                df[token] = df.get(token, 0) + 1
        self._idf = {term: math.log((n + 1) / (freq + 1)) + 1 for term, freq in df.items()}

    def _score(self, query_tokens: List[str], article: Article) -> float:
        """Compute a TF-IDF cosine similarity score between query and article."""
        if not query_tokens or not article.tokens:
            return 0.0

        # Term frequency in article
        article_tf: dict[str, float] = {}
        for token in article.tokens:
            article_tf[token] = article_tf.get(token, 0) + 1
        total = len(article.tokens)
        article_tf = {t: c / total for t, c in article_tf.items()}

        # TF-IDF weight for article
        def tfidf(token: str, tf_map: dict) -> float:
            tf = tf_map.get(token, 0)
            idf = self._idf.get(token, 1.0)
            return tf * idf

        # Dot product between query and article TF-IDF vectors
        q_tf: dict[str, float] = {}
        for token in query_tokens:
            q_tf[token] = q_tf.get(token, 0) + 1
        q_total = len(query_tokens)
        q_tf = {t: c / q_total for t, c in q_tf.items()}

        dot = sum(tfidf(t, q_tf) * tfidf(t, article_tf) for t in q_tf)
        return dot

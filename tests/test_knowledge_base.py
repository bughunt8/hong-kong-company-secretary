"""
Tests for the knowledge base module.
Run with: pytest tests/
"""
import os
import tempfile

import pytest

from app.knowledge_base import Article, KnowledgeBase


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_ARTICLE_1 = """# Company Formation

Company formation in Hong Kong is straightforward. You need a director,
a company secretary, and a registered office address. The Companies Registry
fee is HKD 1720. The process takes 1-3 business days.
"""

SAMPLE_ARTICLE_2 = """# Annual Return

Every Hong Kong company must file an annual return (Form NAR1) within 42 days
of the anniversary of incorporation. Late filing incurs higher fees.
The Companies Registry charges HKD 105 for timely online filing.
"""

SAMPLE_ARTICLE_3 = """# Share Transfer

Shares in a private company can be transferred using a stock transfer form.
Stamp duty of 0.2% of the consideration or market value applies.
The Stamp Duty Office must be notified within 30 days.
"""


@pytest.fixture
def wiki_dir():
    """Create a temporary wiki directory with sample articles."""
    with tempfile.TemporaryDirectory() as tmpdir:
        for name, content in [
            ("01_formation.md", SAMPLE_ARTICLE_1),
            ("02_annual_return.md", SAMPLE_ARTICLE_2),
            ("03_share_transfer.md", SAMPLE_ARTICLE_3),
        ]:
            path = os.path.join(tmpdir, name)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
        yield tmpdir


@pytest.fixture
def kb(wiki_dir):
    knowledge_base = KnowledgeBase(wiki_dir=wiki_dir, top_k=2)
    knowledge_base.load()
    return knowledge_base


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestKnowledgeBaseLoad:
    def test_loads_all_articles(self, kb):
        assert len(kb.articles) == 3

    def test_article_titles_extracted(self, kb):
        titles = [a.title for a in kb.articles]
        assert "Company Formation" in titles
        assert "Annual Return" in titles
        assert "Share Transfer" in titles

    def test_article_filenames(self, kb):
        filenames = [a.filename for a in kb.articles]
        assert "01_formation.md" in filenames

    def test_articles_have_content(self, kb):
        for article in kb.articles:
            assert len(article.content) > 0

    def test_articles_have_tokens(self, kb):
        for article in kb.articles:
            assert len(article.tokens) > 0

    def test_raises_on_missing_directory(self):
        kb_bad = KnowledgeBase(wiki_dir="/nonexistent/path")
        with pytest.raises(FileNotFoundError):
            kb_bad.load()


class TestKnowledgeBaseRetrieval:
    def test_returns_top_k_articles(self, kb):
        results = kb.retrieve("company formation Hong Kong")
        assert len(results) <= kb.top_k

    def test_most_relevant_first(self, kb):
        results = kb.retrieve("annual return filing deadline")
        # The annual return article should score highest
        assert results[0].title == "Annual Return"

    def test_share_transfer_query(self, kb):
        results = kb.retrieve("stamp duty share transfer")
        assert results[0].title == "Share Transfer"

    def test_formation_query(self, kb):
        results = kb.retrieve("how to form a company in Hong Kong director")
        assert results[0].title == "Company Formation"

    def test_empty_query_returns_results(self, kb):
        results = kb.retrieve("")
        # Returns articles but scores may all be 0
        assert isinstance(results, list)

    def test_custom_top_k(self, kb):
        results = kb.retrieve("company", top_k=1)
        assert len(results) == 1

    def test_retrieve_all_with_top_k_exceeding_count(self, kb):
        results = kb.retrieve("hong kong company", top_k=10)
        assert len(results) == 3  # only 3 articles in fixture


class TestArticleExtraction:
    def test_extract_title_from_heading(self):
        content = "# My Title\n\nSome content."
        title = KnowledgeBase._extract_title(content, "fallback.md")
        assert title == "My Title"

    def test_fallback_title_when_no_heading(self):
        content = "No heading here, just text."
        title = KnowledgeBase._extract_title(content, "fallback.md")
        assert title == "fallback.md"

    def test_tokenise_lowercases(self):
        tokens = KnowledgeBase._tokenise("Hello World")
        assert tokens == ["hello", "world"]

    def test_tokenise_removes_punctuation(self):
        tokens = KnowledgeBase._tokenise("HKD 1,720 – annual fee!")
        assert "hkd" in tokens
        assert "1" in tokens
        assert "720" in tokens
        assert "annual" in tokens
        assert "fee" in tokens

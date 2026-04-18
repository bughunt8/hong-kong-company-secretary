"""
LLM client: communicates with an Ollama-compatible API endpoint.
Works with any model served by Ollama, including:
  - llama3, llama2, mistral, gemma
  - Custom/fine-tuned models like Nemoclaw or Openclaw
    (loaded into Ollama as a Modelfile-based custom model)
"""
from __future__ import annotations

import logging
from typing import List

import httpx

from app.knowledge_base import Article

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a professional Hong Kong Company Secretary assistant. \
You answer questions clearly, accurately, and concisely based on Hong Kong \
corporate law and regulatory requirements.

When answering:
- Refer to the relevant legislation (e.g. Companies Ordinance Cap. 622) when appropriate.
- Be practical and specific about deadlines, fees, and procedures.
- If the user asks something outside the scope of Hong Kong company secretarial matters, \
politely redirect them.
- Keep answers concise enough for WhatsApp messaging (aim for under 500 words).

Use the following knowledge base excerpts to inform your answer:
"""


class LLMClient:
    def __init__(self, base_url: str, model: str, timeout: float = 120.0):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    async def generate(self, question: str, context: List[Article]) -> str:
        """
        Generate an answer using the LLM, augmented with retrieved wiki context.
        Falls back to a graceful error message if the LLM is unavailable.
        """
        context_text = self._format_context(context)
        prompt = f"{SYSTEM_PROMPT}\n{context_text}\n\nUser question: {question}\n\nAnswer:"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2,
                "num_predict": 600,
            },
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload,
                )
                response.raise_for_status()
                data = response.json()
                return data.get("response", "").strip()
        except httpx.ConnectError:
            logger.error("Cannot connect to Ollama at %s", self.base_url)
            return (
                "⚠️ The AI model service is currently unavailable. "
                "Please try again later or contact us directly."
            )
        except httpx.HTTPStatusError as exc:
            logger.error("Ollama returned HTTP %s: %s", exc.response.status_code, exc.response.text)
            return "⚠️ An error occurred while generating the answer. Please try again."
        except Exception as exc:  # noqa: BLE001
            logger.exception("Unexpected error calling LLM: %s", exc)
            return "⚠️ An unexpected error occurred. Please try again."

    @staticmethod
    def _format_context(articles: List[Article]) -> str:
        if not articles:
            return "(No specific knowledge base articles found for this query.)"
        parts = []
        for i, article in enumerate(articles, 1):
            # Include up to 1500 chars per article to stay within context window
            snippet = article.content[:1500]
            if len(article.content) > 1500:
                snippet += "\n[…content truncated…]"
            parts.append(f"--- Article {i}: {article.title} ---\n{snippet}")
        return "\n\n".join(parts)

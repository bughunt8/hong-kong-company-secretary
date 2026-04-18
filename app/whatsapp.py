"""
WhatsApp Cloud API (Meta) webhook handler.
Receives incoming WhatsApp messages, queries the knowledge base,
generates answers via the LLM, and sends replies back.
"""
from __future__ import annotations

import logging
from typing import Any

import httpx
from fastapi import HTTPException
from fastapi.responses import PlainTextResponse

from app.knowledge_base import KnowledgeBase
from app.llm_client import LLMClient

logger = logging.getLogger(__name__)

WHATSAPP_API_URL = "https://graph.facebook.com/v19.0/{phone_number_id}/messages"

WELCOME_MESSAGE = (
    "👋 Hello! I'm the Hong Kong Company Secretary Assistant.\n\n"
    "I can answer questions about:\n"
    "• Company incorporation\n"
    "• Annual returns & compliance\n"
    "• Directors & shareholders\n"
    "• Share transfers & stamp duty\n"
    "• Significant Controllers Register\n"
    "• Company dissolution\n"
    "• Business registration\n"
    "• Profits tax obligations\n\n"
    "Just type your question and I'll do my best to help! 🏢"
)


class WhatsAppHandler:
    def __init__(
        self,
        token: str,
        phone_number_id: str,
        verify_token: str,
        knowledge_base: KnowledgeBase,
        llm_client: LLMClient,
    ):
        self.token = token
        self.phone_number_id = phone_number_id
        self.verify_token = verify_token
        self.kb = knowledge_base
        self.llm = llm_client

    # ------------------------------------------------------------------
    # Webhook verification (GET)
    # ------------------------------------------------------------------

    def verify(self, params: dict[str, str]) -> PlainTextResponse:
        mode = params.get("hub.mode")
        token = params.get("hub.verify_token")
        challenge = params.get("hub.challenge")

        if mode == "subscribe" and token == self.verify_token:
            logger.info("WhatsApp webhook verified successfully.")
            return PlainTextResponse(content=challenge, status_code=200)

        logger.warning("WhatsApp webhook verification failed. Params: %s", params)
        raise HTTPException(status_code=403, detail="Webhook verification failed")

    # ------------------------------------------------------------------
    # Incoming message handler (POST)
    # ------------------------------------------------------------------

    async def handle_message(self, body: dict[str, Any]) -> None:
        """Parse the incoming webhook payload and process messages."""
        try:
            entry = body.get("entry", [])
            if not entry:
                return
            changes = entry[0].get("changes", [])
            if not changes:
                return
            value = changes[0].get("value", {})
            messages = value.get("messages", [])
            if not messages:
                return

            msg = messages[0]
            from_number = msg.get("from")
            msg_type = msg.get("type")

            if msg_type == "text":
                text = msg.get("text", {}).get("body", "").strip()
                await self._process_text(from_number, text)
            elif msg_type in ("image", "document", "audio", "video"):
                await self._send_message(
                    from_number,
                    "📄 I can only process text messages at the moment. "
                    "Please type your question as text.",
                )
        except Exception as exc:  # noqa: BLE001
            logger.exception("Error handling WhatsApp message: %s", exc)

    async def _process_text(self, to: str, text: str) -> None:
        lower = text.lower().strip()

        # Greeting detection
        if lower in {"hi", "hello", "hey", "start", "help", "menu"}:
            await self._send_message(to, WELCOME_MESSAGE)
            return

        # Retrieve relevant context and generate answer
        context_articles = self.kb.retrieve(text)
        answer = await self.llm.generate(text, context_articles)

        # Add source references footer
        if context_articles:
            titles = "\n".join(f"  • {a.title}" for a in context_articles)
            footer = f"\n\n📚 _Sources consulted:_\n{titles}"
            answer = answer + footer

        await self._send_message(to, answer)

    # ------------------------------------------------------------------
    # Send message via WhatsApp Cloud API
    # ------------------------------------------------------------------

    async def _send_message(self, to: str, text: str) -> None:
        if not self.token or not self.phone_number_id:
            logger.warning(
                "WHATSAPP_TOKEN or WHATSAPP_PHONE_NUMBER_ID not configured – "
                "skipping message send. Would have sent to %s: %s",
                to, text[:100],
            )
            return

        url = WHATSAPP_API_URL.format(phone_number_id=self.phone_number_id)
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": text},
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, headers=headers, json=payload)
                response.raise_for_status()
                logger.info("Message sent to %s", to)
        except httpx.HTTPStatusError as exc:
            logger.error(
                "Failed to send WhatsApp message to %s: HTTP %s %s",
                to, exc.response.status_code, exc.response.text,
            )
        except Exception as exc:  # noqa: BLE001
            logger.exception("Error sending WhatsApp message: %s", exc)

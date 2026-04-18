"""
Tests for the WhatsApp webhook handler.
"""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi.responses import PlainTextResponse
from fastapi import HTTPException

from app.whatsapp import WhatsAppHandler
from app.knowledge_base import Article


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def mock_kb():
    kb = MagicMock()
    kb.retrieve.return_value = [
        Article(
            filename="01_formation.md",
            title="Company Formation",
            content="Forming a company in HK costs HKD 1720.",
            tokens=["forming", "company", "hk", "costs"],
        )
    ]
    return kb


@pytest.fixture
def mock_llm():
    llm = MagicMock()
    llm.generate = AsyncMock(return_value="You need to pay HKD 1720.")
    return llm


@pytest.fixture
def handler(mock_kb, mock_llm):
    return WhatsAppHandler(
        token="test_token",
        phone_number_id="123456",
        verify_token="test_verify_token",
        knowledge_base=mock_kb,
        llm_client=mock_llm,
    )


# ---------------------------------------------------------------------------
# Webhook verification tests
# ---------------------------------------------------------------------------

class TestWebhookVerify:
    def test_valid_verification(self, handler):
        params = {
            "hub.mode": "subscribe",
            "hub.verify_token": "test_verify_token",
            "hub.challenge": "challenge_abc",
        }
        response = handler.verify(params)
        assert isinstance(response, PlainTextResponse)

    def test_invalid_token_raises_403(self, handler):
        params = {
            "hub.mode": "subscribe",
            "hub.verify_token": "wrong_token",
            "hub.challenge": "challenge_abc",
        }
        with pytest.raises(HTTPException) as exc_info:
            handler.verify(params)
        assert exc_info.value.status_code == 403

    def test_wrong_mode_raises_403(self, handler):
        params = {
            "hub.mode": "unsubscribe",
            "hub.verify_token": "test_verify_token",
            "hub.challenge": "challenge_abc",
        }
        with pytest.raises(HTTPException):
            handler.verify(params)

    def test_missing_params_raises_403(self, handler):
        with pytest.raises(HTTPException):
            handler.verify({})


# ---------------------------------------------------------------------------
# Message handling tests
# ---------------------------------------------------------------------------

class TestHandleMessage:
    @pytest.mark.asyncio
    async def test_greeting_sends_welcome(self, handler):
        with patch.object(handler, "_send_message", new_callable=AsyncMock) as mock_send:
            body = _make_text_payload("hello", "85298765432")
            await handler.handle_message(body)
            mock_send.assert_called_once()
            args = mock_send.call_args[0]
            assert "Hong Kong Company Secretary" in args[1]

    @pytest.mark.asyncio
    async def test_question_triggers_rag(self, handler, mock_kb, mock_llm):
        with patch.object(handler, "_send_message", new_callable=AsyncMock):
            body = _make_text_payload("How do I file an annual return?", "85298765432")
            await handler.handle_message(body)
            mock_kb.retrieve.assert_called_once()
            mock_llm.generate.assert_called_once()

    @pytest.mark.asyncio
    async def test_empty_body_handled_gracefully(self, handler):
        await handler.handle_message({})  # Should not raise

    @pytest.mark.asyncio
    async def test_non_text_message_replied(self, handler):
        with patch.object(handler, "_send_message", new_callable=AsyncMock) as mock_send:
            body = _make_image_payload("85298765432")
            await handler.handle_message(body)
            mock_send.assert_called_once()
            args = mock_send.call_args[0]
            assert "text" in args[1].lower()

    @pytest.mark.asyncio
    async def test_no_token_skips_send(self, mock_kb, mock_llm):
        handler_no_token = WhatsAppHandler(
            token="",
            phone_number_id="",
            verify_token="test_verify_token",
            knowledge_base=mock_kb,
            llm_client=mock_llm,
        )
        # Should not raise even without token configured
        await handler_no_token._send_message("85298765432", "test message")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_text_payload(text: str, from_number: str) -> dict:
    return {
        "entry": [
            {
                "changes": [
                    {
                        "value": {
                            "messages": [
                                {
                                    "from": from_number,
                                    "type": "text",
                                    "text": {"body": text},
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }


def _make_image_payload(from_number: str) -> dict:
    return {
        "entry": [
            {
                "changes": [
                    {
                        "value": {
                            "messages": [
                                {
                                    "from": from_number,
                                    "type": "image",
                                    "image": {"id": "img123"},
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }

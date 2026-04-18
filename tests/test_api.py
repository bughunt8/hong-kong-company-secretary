"""
Integration tests for the FastAPI application endpoints.
"""
import os
import tempfile
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

# We need to set up environment before importing app
SAMPLE_WIKI_CONTENT = """# Company Formation in Hong Kong

Company formation requires a director, company secretary, and registered office.
The fee is HKD 1720. Takes 1-3 business days via Companies Registry.
"""


@pytest.fixture
def wiki_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "01_formation.md"), "w") as fh:
            fh.write(SAMPLE_WIKI_CONTENT)
        yield tmpdir


@pytest.fixture
def test_client(wiki_dir):
    with patch.dict(
        os.environ,
        {
            "WIKI_DIR": wiki_dir,
            "OLLAMA_URL": "http://localhost:99999",  # intentionally unreachable
            "LLM_MODEL": "llama3",
            "WHATSAPP_TOKEN": "",
            "WHATSAPP_PHONE_NUMBER_ID": "",
            "WHATSAPP_VERIFY_TOKEN": "test_token",
        },
    ):
        from app.main import app
        with TestClient(app) as client:
            yield client


class TestHealthEndpoint:
    def test_health_returns_ok(self, test_client):
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["articles"] >= 1


class TestArticlesEndpoint:
    def test_list_articles_returns_list(self, test_client):
        response = test_client.get("/articles")
        assert response.status_code == 200
        articles = response.json()
        assert isinstance(articles, list)
        assert len(articles) >= 1

    def test_articles_have_title_and_filename(self, test_client):
        response = test_client.get("/articles")
        for article in response.json():
            assert "title" in article
            assert "filename" in article


class TestAskEndpoint:
    def test_ask_returns_answer(self, test_client):
        with patch("app.llm_client.LLMClient.generate", new_callable=AsyncMock) as mock_gen:
            mock_gen.return_value = "The fee is HKD 1720."
            response = test_client.post(
                "/ask",
                json={"question": "How much does it cost to form a company?"},
            )
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "question" in data
        assert "context_titles" in data

    def test_ask_missing_question_returns_400(self, test_client):
        response = test_client.post("/ask", json={})
        assert response.status_code == 400

    def test_ask_empty_question_returns_400(self, test_client):
        response = test_client.post("/ask", json={"question": ""})
        assert response.status_code == 400


class TestWebhookEndpoint:
    def test_webhook_verify_challenge(self, test_client):
        response = test_client.get(
            "/webhook",
            params={
                "hub.mode": "subscribe",
                "hub.verify_token": "test_token",
                "hub.challenge": "challenge_xyz",
            },
        )
        assert response.status_code == 200
        assert response.text == "challenge_xyz"

    def test_webhook_verify_wrong_token(self, test_client):
        response = test_client.get(
            "/webhook",
            params={
                "hub.mode": "subscribe",
                "hub.verify_token": "wrong_token",
                "hub.challenge": "challenge_xyz",
            },
        )
        assert response.status_code == 403

    def test_webhook_post_returns_ok(self, test_client):
        with patch("app.whatsapp.WhatsAppHandler._send_message", new_callable=AsyncMock):
            with patch("app.llm_client.LLMClient.generate", new_callable=AsyncMock) as mock_gen:
                mock_gen.return_value = "Test answer."
                response = test_client.post(
                    "/webhook",
                    json={
                        "entry": [
                            {
                                "changes": [
                                    {
                                        "value": {
                                            "messages": [
                                                {
                                                    "from": "85298765432",
                                                    "type": "text",
                                                    "text": {"body": "How do I form a company?"},
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                )
        assert response.status_code == 200

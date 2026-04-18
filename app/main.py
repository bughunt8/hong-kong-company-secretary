"""
Hong Kong Company Secretary LLM Knowledge Base
Entry point for the FastAPI application.
"""
import os
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from app.knowledge_base import KnowledgeBase
from app.llm_client import LLMClient
from app.whatsapp import WhatsAppHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Global singletons – initialised once at startup
# ---------------------------------------------------------------------------
kb: KnowledgeBase | None = None
llm: LLMClient | None = None
wa_handler: WhatsAppHandler | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global kb, llm, wa_handler

    wiki_dir = os.environ.get("WIKI_DIR", "wiki")
    logger.info("Loading knowledge base from %s …", wiki_dir)
    kb = KnowledgeBase(wiki_dir)
    kb.load()

    ollama_url = os.environ.get("OLLAMA_URL", "http://ollama:11434")
    model_name = os.environ.get("LLM_MODEL", "llama3")
    llm = LLMClient(base_url=ollama_url, model=model_name)

    wa_token = os.environ.get("WHATSAPP_TOKEN", "")
    wa_phone_id = os.environ.get("WHATSAPP_PHONE_NUMBER_ID", "")
    wa_verify_token = os.environ.get("WHATSAPP_VERIFY_TOKEN", "hkcs_verify")
    wa_handler = WhatsAppHandler(
        token=wa_token,
        phone_number_id=wa_phone_id,
        verify_token=wa_verify_token,
        knowledge_base=kb,
        llm_client=llm,
    )

    logger.info("Application ready.")
    yield
    logger.info("Application shutting down.")


app = FastAPI(
    title="HK Company Secretary LLM Bot",
    description="RAG-powered WhatsApp bot for Hong Kong company secretary questions.",
    version="1.0.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------------------------
# Health / info endpoints
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    return {"status": "ok", "articles": len(kb.articles) if kb else 0}


@app.get("/articles")
async def list_articles():
    if not kb:
        raise HTTPException(status_code=503, detail="Knowledge base not loaded")
    return [{"title": a.title, "filename": a.filename} for a in kb.articles]


@app.post("/ask")
async def ask(request: Request):
    """Direct HTTP endpoint for asking questions (useful for testing)."""
    body = await request.json()
    question = body.get("question", "").strip()
    if not question:
        raise HTTPException(status_code=400, detail="'question' field is required")

    context = kb.retrieve(question)
    answer = await llm.generate(question, context)
    return {"question": question, "answer": answer, "context_titles": [a.title for a in context]}


# ---------------------------------------------------------------------------
# WhatsApp Cloud API webhook endpoints
# ---------------------------------------------------------------------------

@app.get("/webhook")
async def whatsapp_verify(request: Request):
    """WhatsApp webhook verification (GET challenge)."""
    params = dict(request.query_params)
    return wa_handler.verify(params)


@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    """Receive incoming WhatsApp messages."""
    body = await request.json()
    await wa_handler.handle_message(body)
    return Response(content="OK", status_code=200)

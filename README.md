# Hong Kong Company Secretary LLM Knowledge Base

A **Docker-based RAG (Retrieval-Augmented Generation) chatbot** that answers Hong Kong company secretary questions via WhatsApp.  
The system uses a local LLM (served via [Ollama](https://ollama.com/)) to answer questions grounded in a structured markdown knowledge base, following the [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern.

---

## Architecture

```
WhatsApp User
     │
     ▼ (HTTPS)
WhatsApp Cloud API (Meta)
     │
     ▼ (webhook POST /webhook)
┌────────────────────────────────────────────────┐
│  FastAPI App (app/)                            │
│  ├── knowledge_base.py  → TF-IDF retrieval    │
│  ├── llm_client.py      → Ollama API client   │
│  └── whatsapp.py        → Webhook handler     │
└────────────────────────────────────────────────┘
     │
     ▼ (http://ollama:11434)
┌──────────────────────┐
│  Ollama              │
│  (LLaMA 3 / Nemoclaw │
│   / Openclaw / etc.) │
└──────────────────────┘
     │ (context grounding)
┌──────────────────────┐
│  wiki/               │
│  15 Markdown articles│
│  on HK company law   │
└──────────────────────┘
```

---

## Knowledge Base (wiki/)

15 wiki articles covering the key topics of Hong Kong company secretary practice:

| File | Topic |
|------|-------|
| `01_company_formation.md` | Incorporation process, requirements, costs |
| `02_company_secretary.md` | Role, duties, and qualifications |
| `03_registered_office.md` | Requirements, SAIL, changing address |
| `04_directors_and_officers.md` | Director duties, appointment, removal |
| `05_share_capital.md` | Share types, shareholders, allotments |
| `06_annual_return.md` | Form NAR1, deadlines, fees |
| `07_annual_general_meeting.md` | AGM requirements, notice, resolutions |
| `08_business_registration.md` | BRC, renewal, BRN |
| `09_statutory_records.md` | Registers that must be maintained |
| `10_significant_controllers_register.md` | SCR requirements, 25% threshold |
| `11_company_dissolution.md` | Deregistration, winding up |
| `12_change_of_company_name.md` | Process and restrictions |
| `13_transfer_of_shares.md` | Stamp duty, STF, process |
| `14_profits_tax.md` | Tax obligations, two-tier rates |
| `15_compliance_calendar.md` | All key deadlines in one place |

---

## Quick Start

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and Docker Compose
- A [Meta for Developers](https://developers.facebook.com/) account for WhatsApp Cloud API (optional – bot works without it for local `/ask` API testing)
- A publicly accessible URL for the webhook (e.g. via [ngrok](https://ngrok.com/))

### 1. Clone and configure

```bash
git clone https://github.com/bughunt8/hong-kong-company-secretary.git
cd hong-kong-company-secretary
cp .env.example .env
```

Edit `.env` and fill in:
- `WHATSAPP_TOKEN` – Your WhatsApp Bearer token from Meta
- `WHATSAPP_PHONE_NUMBER_ID` – Your WhatsApp phone number ID
- `WHATSAPP_VERIFY_TOKEN` – Any secret string you choose
- `LLM_MODEL` – Model name (default: `llama3`)

### 2. Start the stack

```bash
docker compose up -d
```

This starts:
- **ollama** – LLM inference server (downloads the model on first run)
- **ollama-init** – One-time model pull (exits after completing)
- **app** – The FastAPI bot server on port `8000`

### 3. Test locally

```bash
# Health check
curl http://localhost:8000/health

# Ask a question directly
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I file an annual return in Hong Kong?"}'

# List all knowledge base articles
curl http://localhost:8000/articles
```

### 4. Connect WhatsApp

1. Expose your server via ngrok or a cloud host:
   ```bash
   ngrok http 8000
   ```
2. In the [Meta Developer Console](https://developers.facebook.com/):
   - Go to your WhatsApp app → Configuration → Webhooks
   - Set **Callback URL**: `https://<your-ngrok-url>/webhook`
   - Set **Verify Token**: the value from `WHATSAPP_VERIFY_TOKEN` in your `.env`
   - Subscribe to `messages`
3. Send a WhatsApp message to your business number. The bot will reply.

---

## Using Custom Models (Nemoclaw / Openclaw)

If you have a custom model (e.g. a legal-domain fine-tune like Nemoclaw or Openclaw), load it into Ollama using a `Modelfile`:

```
# Modelfile.nemoclaw
FROM llama3
SYSTEM "You are Nemoclaw, a Hong Kong legal assistant specialised in company law."
```

```bash
# Build the custom model in the running Ollama container
docker exec hkcs_ollama ollama create nemoclaw -f /path/to/Modelfile.nemoclaw

# Update LLM_MODEL in .env
LLM_MODEL=nemoclaw

# Restart the app
docker compose restart app
```

Alternatively, if you have a GGUF model file:
```
FROM /models/nemoclaw.gguf
PARAMETER temperature 0.2
```

---

## Production Deployment

For production, enable the Nginx reverse proxy with SSL:

```bash
# Place your SSL certificates in nginx/certs/
mkdir -p nginx/certs
# Copy cert.pem and key.pem into nginx/certs/

docker compose --profile production up -d
```

Update `nginx/nginx.conf` to add HTTPS:
```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/nginx/certs/cert.pem;
    ssl_certificate_key /etc/nginx/certs/key.pem;
    ...
}
```

---

## Development

### Run tests

```bash
pip install -r requirements.txt pytest pytest-asyncio
pytest tests/ -v
```

### Project structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app and routes
│   ├── knowledge_base.py  # Wiki loading and TF-IDF retrieval
│   ├── llm_client.py      # Ollama API client
│   └── whatsapp.py        # WhatsApp Cloud API webhook handler
├── wiki/                  # Markdown knowledge base articles
├── tests/                 # pytest test suite
├── nginx/
│   └── nginx.conf         # Optional reverse proxy config
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_URL` | `http://ollama:11434` | Ollama server URL |
| `LLM_MODEL` | `llama3` | Model name in Ollama |
| `WIKI_DIR` | `/app/wiki` | Path to wiki markdown files |
| `RETRIEVAL_TOP_K` | `3` | Number of articles retrieved per query |
| `WHATSAPP_TOKEN` | _(required)_ | WhatsApp Cloud API bearer token |
| `WHATSAPP_PHONE_NUMBER_ID` | _(required)_ | WhatsApp phone number ID |
| `WHATSAPP_VERIFY_TOKEN` | `hkcs_verify` | Webhook verification secret |

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check and article count |
| `GET` | `/articles` | List all knowledge base articles |
| `POST` | `/ask` | Ask a question (JSON: `{"question": "..."}`) |
| `GET` | `/webhook` | WhatsApp webhook verification |
| `POST` | `/webhook` | Receive WhatsApp messages |

---

## Disclaimer

This bot provides general information about Hong Kong company secretarial requirements. It is not legal advice. Always consult a qualified Hong Kong company secretary or solicitor for specific matters.

---

## Licence

Apache 2.0 – see [LICENSE](LICENSE).

FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and wiki knowledge base
COPY app/ ./app/
COPY wiki/ ./wiki/

# Expose the web server port
EXPOSE 8000

# Default environment variable – override in docker-compose.yml or .env
ENV WIKI_DIR=/app/wiki \
    OLLAMA_URL=http://ollama:11434 \
    LLM_MODEL=llama3 \
    WHATSAPP_VERIFY_TOKEN=hkcs_verify

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

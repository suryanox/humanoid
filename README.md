# Humanoid

AI-powered human-like persona simulator for conversations.

## Setup

1. **Install Poetry**
```bash
pip install poetry

```


2. **Install Dependencies**
```bash
poetry install

```

## Configuration

Open `.env` file to configure your model provider.

This project uses the [LiteLLM Python SDK](https://docs.litellm.ai/docs/#litellm-python-sdk), which means any provider supported by LiteLLM is supported here by default.

* **For Cloud Providers:** Set your `API_KEY` and/or `BASE_URL` (e.g., `OPENAI_API_KEY`).
* **For Ollama:** No setup is required; just ensure Ollama is running locally.

## Run

```bash
poetry run uvicorn humanoid.main:app --reload

```

---

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

Open `.env` file (in the root of project) to configure your model provider.

This project uses the [LiteLLM Python SDK](https://docs.litellm.ai/docs/#litellm-python-sdk), which means any provider supported by LiteLLM is supported here by default.

* **For Cloud Providers:** Set your `API_KEY` and/or `BASE_URL` (e.g., `OPENAI_API_KEY`).
* **For Ollama:** No setup is required; just ensure Ollama is running locally.

## Run

```bash
poetry run uvicorn humanoid.main:app --reload

```

---

## Example Usage Flow

### 1. Initiate Interaction

Call this once to set the persona and context. This returns a `session_id` and the persona's opening line.

**Request:**

```bash
curl --location 'http://127.0.0.1:8000/api/v1/initiate_interaction' \
--header 'Content-Type: application/json' \
--data '{
    "persona": {
        "name": "Alex",
        "role": "disappointed customer",
        "tone": "frustrated",
        "adherence": 0.8
    },
    "context": "The smart watch I ordered arrived with a cracked screen. Order #9982.",
    "model": "gpt-4o",
    "language_code" : "en"
}'

```

**Response:**

```json
{
    "session_id": "e8e32501-429b-4d52-91be-84f1e8798d04",
    "first_reply": "I just opened my package for order #9982 and the screen is completely cracked. This is unacceptable. How do you plan to fix this immediately?"
}

```

### 2. Ongoing Interaction

Use the `session_id` to continue the conversation.

**Message 2: Denying immediate refund**

```bash
curl --location 'http://127.0.0.1:8000/api/v1/interact/e8e32501-429b-4d52-91be-84f1e8798d04' \
--header 'Content-Type: application/json' \
--data '{ "message": "I apologize, but we need to inspect the device before issuing a refund." }'

```

> **Response:** "Inspect it? I sent you photos of the damage! I shouldn't have to wait weeks for a refund on a product that arrived broken. Is there a manager I can speak to?"

**Message 3: Offering a replacement instead**

```bash
curl --location 'http://127.0.0.1:8000/api/v1/interact/e8e32501-429b-4d52-91be-84f1e8798d04' \
--header 'Content-Type: application/json' \
--data '{ "message": "We can ship a replacement today if you prefer that over a refund." }'

```

> **Response:** "If you ship it today via express mail, I might consider it. But I need a tracking number within the hour. Can you guarantee that?"

**Message 4: Checking stock**

```bash
curl --location 'http://127.0.0.1:8000/api/v1/interact/e8e32501-429b-4d52-91be-84f1e8798d04' \
--header 'Content-Type: application/json' \
--data '{ "message": "Let me check the stock... actually, that model is currently backordered for 2 weeks." }'

```

> **Response:** "Unbelievable. First it's broken, now it's out of stock? Just give me the refund. I'll buy it somewhere else that actually has quality control."

---

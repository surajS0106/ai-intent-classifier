Here’s a complete `README.md` for your **InfraGenie Prompt Intent Guard** project using **DeepSeek**, **FastAPI**, and **OpenAI-compatible SDK**:

---

````markdown
# 🔐 InfraGenie Prompt Intent Guard (DeepSeek + FastAPI)

This is a Proof of Concept (PoC) API that filters and allows only **infrastructure-related** prompts (like Terraform or AWS provisioning) to proceed. If a user submits a general or unrelated query (e.g., a poem, joke, or bird fact), the app rejects it gracefully.

---

## 🧠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) – Web API Framework
- [DeepSeek](https://deepseek.com/) – OpenAI-compatible LLM
- [Python OpenAI SDK](https://pypi.org/project/openai/) – For calling DeepSeek
- [python-dotenv](https://pypi.org/project/python-dotenv/) – For environment variables

---

## ⚙️ Features

- Classifies user prompts into `infrastructure` or `non-infra`
- Only processes prompts related to Terraform, AWS, DevOps, etc.
- Returns an error for anything else
- Easily extendable with full LLM-based output

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/infragenie-intent-guard.git
cd infragenie-intent-guard
````

### 2. Create `.env` file

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 3. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
uvicorn main:app --reload
```

---

## 📬 Example API Usage

### ✅ Infra Prompt

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write Terraform code for an S3 bucket."}'
```

**Response:**

```json
{
  "status": "success",
  "response": "✅ Infra request accepted! Here's your Terraform code for an AWS EC2 instance..."
}
```

---

### ❌ Non-Infra Prompt

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write me a poem about the stars"}'
```

**Response:**

```json
{
  "status": "rejected",
  "message": "❌ Invalid prompt. You can only ask about Terraform or Infrastructure-related topics."
}
```

---

## 📄 File Structure

```
.
├── main.py            # FastAPI main app
├── intent_guard.py    # Prompt classifier using DeepSeek
├── .env               # API key (never commit this)
└── requirements.txt   # Dependencies
```

---

## 🧪 Future Ideas

* Frontend form for prompt submission
* User/IP tracking for abuse
* Generate full Terraform code from valid prompts
* Dockerize for deployment

---

## 🛡️ License

MIT License © 2025 \[Your Name]

```

---

Let me know if you want me to auto-generate this in your actual project folder (with file-writing code) or if you're deploying this to GitHub and want a badge-filled version.
```

from fastapi import FastAPI
from pydantic import BaseModel
from intent_guard import classify_prompt

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/ask")
async def ask_infragenie(input: PromptInput):
    intent = await classify_prompt(input.prompt)

    if intent == "infrastructure":
        return {
            "status": "success",
            "response": "✅ Infra request accepted! Here's your Terraform code for an AWS EC2 instance..."
        }
    elif intent == "non-infra":
        return {
            "status": "rejected",
            "message": "❌ Invalid prompt. You can only ask about Terraform or Infrastructure-related topics."
        }
    else:
        return {
            "status": "error",
            "message": "⚠️ Could not process the prompt due to an error."
        }

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

async def classify_prompt(prompt: str) -> str:
    system_prompt = """
    You are a strict classifier. Categorize the user's prompt into one of the following:
    ["infrastructure", "non-infra"]

    Classify as:
    - "infrastructure" if the prompt is about terraform, cloud, infrastructure, devops, provisioning etc.
    - "non-infra" if it's about poetry, animals, jokes, birds, personal questions, etc.

    Reply with one word only: infrastructure or non-infra.
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt.strip()},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        return response.choices[0].message.content.strip().lower()
    except Exception as e:
        print("Error:", str(e))
        return "error"

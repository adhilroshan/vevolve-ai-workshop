"""Prompt Technique 4: Constrained Output prompting.
Day 1, Session 2: Prompt Engineering
Learning Objective: Force LLM to return specific formats (JSON).
"""

import json
import os

import dotenv
import openai


def load_env():
    """Load environment variables from .env file. Returns True if successful."""
    dotenv.load_dotenv()
    return os.path.exists(".env")


def main():
    load_env()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    client = openai.OpenAI(base_url=os.getenv("OPENAI_BASE_URL"), api_key=api_key)

    prompt = """
    Return a JSON object with keys: status (PASS/FAIL), message (string), timestamp (ISO format).
    Do not include any text outside the JSON object.
    """

    response = client.chat.completions.create(
        model="tencent/hy3-preview:free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        response_format={"type": "json_object"},
    )

    print("Constrained JSON Output:")
    print(response.choices[0].message.content)
    data = json.loads(response.choices[0].message.content)
    print("Parsed JSON:", data)


if __name__ == "__main__":
    main()

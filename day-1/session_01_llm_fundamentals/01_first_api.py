"""Simplest possible LLM call using the current OpenAI SDK.
Day 1, Session 1: LLM Fundamentals Part B
Learning Objective: Make a basic Responses API call.
"""

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

    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[
            {
                "role": "user",
                "content": "Write a three-sentence opening for a sci-fi novel about a planet where it only rains glass.",
            },
        ],
        max_completion_tokens=10,
        temperature=0.9,
    )
    print("Chatbot Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

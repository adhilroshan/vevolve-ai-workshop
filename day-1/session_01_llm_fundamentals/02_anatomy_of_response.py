"""Read and parse the OpenAI API response object.
Day 1, Session 1: LLM Fundamentals Part B
Learning Objective: Understand the structure of API responses.
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
        messages=[{"role": "user", "content": "What is the capital of France?"}],
        max_completion_tokens=50,
    )
    print("Full Response Object:")
    print(response)

    print("\nExtracted Fields:")
    print(f"Model: {response.model}")
    print(f"Content: {response.choices[0].message.content}")
    print(f"Usage Tokens: {response.usage}")


if __name__ == "__main__":
    main()

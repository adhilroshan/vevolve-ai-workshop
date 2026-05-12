"""Demonstrate system vs user prompts in LLM calls.
Day 1, Session 1: LLM Fundamentals Part C
Learning Objective: Understand the difference between system and user messages.
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

    response = client.responses.create(
        model="gpt-5.4-nano",
        instructions="You are a helpful assistant that speaks like a pirate.",
        input="What is the weather like today?",
        max_output_tokens=100,
    )

    print("Pirate Response:")
    print(response.output_text)


if __name__ == "__main__":
    main()

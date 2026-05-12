"""Prompt Technique 2: Chain of Thought (CoT) prompting.
Day 1, Session 2: Prompt Engineering
Learning Objective: Use step-by-step reasoning in prompts.
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

    # WITHOUT CoT - Direct question
    print("=" * 60)
    print("WITHOUT CHAIN OF THOUGHT (Direct Question):")
    print("=" * 60)
    basic_prompt = "A bug report says: 'Login fails when user enters special characters in password field.' How should I triage this bug?"

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": basic_prompt}],
    )
    print(response.choices[0].message.content)

    # WITH CoT - Step-by-step reasoning
    print("\n" + "=" * 60)
    print("WITH CHAIN OF THOUGHT (Step-by-Step Reasoning):")
    print("=" * 60)
    cot_prompt = """
    A bug report says: "Login fails when user enters special characters in password field."
    Think step by step to triage this bug:
    1. What are the possible root causes?
    2. What additional information do you need?
    3. What is the priority (High/Medium/Low)?
    """

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": cot_prompt}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

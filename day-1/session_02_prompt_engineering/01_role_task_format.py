"""Prompt Technique 1: Role-Task-Format (RTF) prompting.
Day 1, Session 2: Prompt Engineering
Learning Objective: Structure prompts with clear role, task, and format.
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

    # WITHOUT RTF - Basic prompt
    print("=" * 60)
    print("WITHOUT RTF (Basic Prompt):")
    print("=" * 60)
    basic_prompt = "Write test cases for a login form."

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": basic_prompt}],
    )
    print(response.choices[0].message.content)

    # WITH RTF - Structured prompt
    print("\n" + "=" * 60)
    print("WITH RTF (Role-Task-Format):")
    print("=" * 60)
    rtf_prompt = """
    Role: You are a senior QA engineer.
    Task: Write 3 test cases for a login form with username and password fields.
    Format: Numbered list, each test case has: ID, Steps, Expected Result.
    """

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": rtf_prompt}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

"""Demonstrate stateless LLM API calls (no memory).
Day 2, Session 3: Conversational Memory Part A
Learning Objective: Understand that LLMs are stateless by default.
"""

import os

from common import check_env
from openai import OpenAI


def main():
    check_env()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # First call: introduce user
    prompt1 = "My name is Alice."
    print("Prompt 1:", prompt1)

    response1 = client.responses.create(
        model="gpt-5.4-nano",
        input=[{"role": "user", "content": prompt1}],
        max_output_tokens=500,
    )
    text1 = response1.output_text
    print("Response 1:", text1)

    # Second call: ask name without context
    prompt2 = "What is my name?"
    print("\nPrompt 2:", prompt2)
    response2 = client.responses.create(
        model="gpt-5.4-nano",
        input=[{"role": "user", "content": prompt2}],
        max_output_tokens=500,
    )
    text2 = response2.output_text
    print("Response 2:", text2)


if __name__ == "__main__":
    main()

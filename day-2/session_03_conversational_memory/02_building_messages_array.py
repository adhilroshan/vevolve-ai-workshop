"""Build persistent message history for LLM conversations.
Day 2, Session 3: Conversational Memory Part B
Learning Objective: Maintain conversation context with message arrays.
"""

import os

from common import check_env
from openai import OpenAI


def main():
    check_env()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-nano")
    messages = []

    # Add user message
    messages.append({"role": "user", "content": "My name is Bob."})
    print("Prompt 1:", messages[-1]["content"])

    response = client.responses.create(model=model, input=messages)
    print("Response 1:", response.output_text)

    # Add assistant response to history
    messages.append({"role": "assistant", "content": response.output_text})

    # Ask name again with context
    messages.append({"role": "user", "content": "What is my name?"})
    print("\nPrompt 2:", messages[-1]["content"])

    response = client.responses.create(model=model, input=messages)
    print("Response 2:", response.output_text)


if __name__ == "__main__":
    main()

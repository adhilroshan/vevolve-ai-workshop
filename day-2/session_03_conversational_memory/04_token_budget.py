"""Manage token budget for long conversations.
Day 2, Session 3: Conversational Memory Part B
Learning Objective: Implement message truncation to avoid token limits.
"""

import os

from common import check_env
from openai import OpenAI


def truncate_messages(messages, max_messages=10):
    """Keep only the last max_messages to stay within token budget."""
    return messages[-max_messages:] if len(messages) > max_messages else messages


def main():
    check_env()
    client = OpenAI(
        base_url=os.getenv("OPENAI_BASE_URL"), api_key=os.getenv("OPENAI_API_KEY")
    )
    model = os.getenv("OPENAI_MODEL", "tencent/hy3-preview:free")
    messages = []

    # Simulate long conversation
    for i in range(15):
        messages.append({"role": "user", "content": f"Message {i}"})
        messages.append({"role": "assistant", "content": f"Response {i}"})

    print(f"Original message count: {len(messages)}")
    truncated = truncate_messages(messages, max_messages=10)
    print(f"Truncated message count: {len(truncated)}")


if __name__ == "__main__":
    main()

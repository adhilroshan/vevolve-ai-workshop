"""Manage token budget for long conversations with actual API calls.
Day 2, Session 3: Conversational Memory Part B (Complete Version)
Learning Objective: Implement message truncation to avoid token limits.
"""

import os

from common import check_env
from openai import OpenAI


def truncate_messages(messages, max_messages=10):
    """Keep only the last max_messages to stay within token budget."""
    return messages[-max_messages:] if len(messages) > max_messages else messages


def get_conversation_summary(client, model, messages):
    """Summarise older messages to save token budget (advanced technique)."""
    summary_prompt = (
        "Summarise the following conversation history concisely, "
        "preserving key facts and decisions:\n\n"
        + "\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in messages)
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": summary_prompt}],
        max_tokens=100,
    )
    return response.choices[0].message.content


def chat_with_memory(user_input, messages, client, model, max_messages=10):
    """
    Send user input to the model with conversation history.
    Truncates messages if the conversation grows beyond the token budget.
    """
    # Add the new user message
    messages.append({"role": "user", "content": user_input})

    # Truncate if we exceed the max message count
    if len(messages) > max_messages:
        print(
            f"⚠️  Conversation too long ({len(messages)} messages). Truncating to last {max_messages}..."
        )
        messages = truncate_messages(messages, max_messages=max_messages)

    # Send to the AI model
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=150,
    )

    # Get the assistant's reply
    assistant_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply, messages


def main():
    check_env()
    client = OpenAI(
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    model = os.getenv("OPENAI_MODEL", "tencent/hy3-preview:free")
    messages = []

    print("=== Conversational Memory with Token Budget Management ===")
    print(f"Using model: {model}")
    print("Type 'quit' to exit.\n")

    # Simulate a long conversation
    for i in range(15):
        user_msg = f"Tell me a fun fact about number {i}"
        print(f"\n--- Turn {i + 1} ---")
        print(f"User: {user_msg}")

        reply, messages = chat_with_memory(
            user_msg, messages, client, model, max_messages=10
        )
        print(f"Assistant: {reply}")
        print(f"Conversation length: {len(messages)} messages")

    print("\n=== Conversation Complete ===")
    print(f"Final message count: {len(messages)}")
    print("\nFull conversation:")
    for msg in messages:
        print(f"  {msg['role'].capitalize()}: {msg['content']}")


if __name__ == "__main__":
    main()

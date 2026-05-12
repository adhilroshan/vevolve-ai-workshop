"""
Chatbot that uses conversational memory to maintain context and provide relevant responses.
"""

import os

from common import check_env
from openai import OpenAI


def main():
    check_env()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-nano")
    messages = []

    print("Chat with the bot (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        messages.append({"role": "user", "content": user_input})
        response = client.responses.create(
            model=model, input=messages, max_output_tokens=150
        )
        assistant_response = response.output_text
        messages.append({"role": "assistant", "content": assistant_response})
        print("Bot:", assistant_response)


if __name__ == "__main__":
    main()

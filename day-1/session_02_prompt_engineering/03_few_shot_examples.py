"""Prompt Technique 3: Few-Shot Prompting.
Day 1, Session 2: Prompt Engineering
Learning Objective: Provide examples to guide LLM output.
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

    # WITHOUT Few-Shot - Direct instruction only
    print("=" * 60)
    print("WITHOUT FEW-SHOT (Direct Instruction):")
    print("=" * 60)
    basic_prompt = "Extract the name and age from the text: 'Charlie is 40 years old.'"
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": basic_prompt}],
    )
    print(response.choices[0].message.content)

    # WITH Few-Shot - Provide examples
    print("\n" + "=" * 60)
    print("WITH FEW-SHOT (Examples Provided):")
    print("=" * 60)
    few_shot_prompt = """
    Extract the name and age from the text.

    Example 1:
    Text: \"Alice is 30 years old.\"
    Output: {"name": "Alice", "age": 30}

    Example 2:
    Text: \"Bob is 25 years old.\"
    Output: {"name": "Bob", "age": 25}

    Text: \"Charlie is 40 years old.\"
    Output:
    """
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": few_shot_prompt}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

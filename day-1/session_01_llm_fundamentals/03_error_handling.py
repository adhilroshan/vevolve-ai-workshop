"""Handle common OpenAI API errors.
Day 1, Session 1: LLM Fundamentals Part B
Learning Objective: Implement error handling for API calls.
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
    try:
        response = client.responses.create(
            model="gpt-5.4-nano",
            input="Test error handling",
            max_output_tokens=50,
        )
        print("Success:", response.output_text)
    except openai.AuthenticationError:
        print("Error: Invalid API key")
    except openai.RateLimitError:
        print("Error: Rate limit exceeded")
    except openai.APIError as e:
        print(f"Error: API error occurred: {e}")


if __name__ == "__main__":
    main()

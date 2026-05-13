"""Enforce structured output with JSON Schema.
Day 2, Session 4: Structured Outputs Part A
Learning Objective: Use schema-shaped output for code-readable responses.
"""

import json
import os

from common import check_env
from openai import OpenAI

PERSON_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["name", "age"],
    "additionalProperties": False,
}


def main():
    check_env()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    data = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.4-nano"),
        instructions="Return only data that matches the provided JSON schema.",
        input="Extract this person: Priya is 34 years old.",
        text={
            "format": {
                "type": "json_schema",
                "name": "person",
                "schema": PERSON_SCHEMA,
                "strict": True,
            }
        },
    )
    print("JSON Output:", data.output_text)

    result = json.loads(data.output_text)
    print("Parsed Output:", result)


if __name__ == "__main__":
    main()

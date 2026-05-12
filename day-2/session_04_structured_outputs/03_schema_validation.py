"""Validate JSON responses against a Python schema.
Day 2, Session 4: Structured Outputs Part A
Learning Objective: Validate structured output with Python types.
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


def validate_schema(data):
    """Check if data has required keys and types."""
    required = {"name": str, "age": int}
    for key, type_ in required.items():
        if key not in data:
            return False, f"Missing key: {key}"
        if not isinstance(data[key], type_):
            return False, f"Wrong type for {key}: expected {type_}"
    return True, "Valid"


def main():
    check_env()
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        instructions="Return only data that matches the provided JSON schema.",
        input="Extract this person: Omar is 41 years old.",
        text={
            "format": {
                "type": "json_schema",
                "name": "person",
                "schema": PERSON_SCHEMA,
                "strict": True,
            }
        },
    )
    json_str = response.output_text
    data = json.loads(json_str)
    valid, msg = validate_schema(data)
    print(f"Validation: {msg}, Data: {data}")


if __name__ == "__main__":
    main()

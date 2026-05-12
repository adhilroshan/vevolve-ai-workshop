"""Parse and handle JSON API responses.
Day 2, Session 4: Structured Outputs Part A
Learning Objective: Safely parse JSON from LLM responses.
"""

import json
import os

from common import check_env
from openai import OpenAI

STATUS_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["PASS", "FAIL"]},
    },
    "required": ["status"],
    "additionalProperties": False,
}


def main():
    check_env()
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-3.5"),
        instructions="Return only data that matches the provided JSON schema.",
        input="Return a status of PASS.",
        text={
            "format": {
                "type": "json_schema",
                "name": "status_result",
                "schema": STATUS_SCHEMA,
                "strict": True,
            }
        },
    )
    # Extract the text content from the response
    json_str = response.output_text
    try:
        data = json.loads(json_str)
        print("Parsed JSON:", data)
    except json.JSONDecodeError as e:
        print("JSON Parse Error:", e)


if __name__ == "__main__":
    main()

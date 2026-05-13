"""Structured output pattern: extract, validate, and retry once."""

import json
import os
import sys
from pathlib import Path

from common import check_env
from openai import OpenAI

sys.path.append(str(Path(__file__).resolve().parents[2]))


TICKET_SCHEMA = {
    "type": "object",
    "properties": {
        "customer_name": {"type": "string"},
        "category": {"type": "string", "enum": ["auth", "billing", "bug", "other"]},
        "urgency": {"type": "string", "enum": ["low", "medium", "high"]},
        "issue": {"type": "string"},
        "next_action": {"type": "string"},
    },
    "required": ["customer_name", "category", "urgency", "issue", "next_action"],
    "additionalProperties": False,
}


def ask_json(prompt, schema, *, name="result"):
    check_env()
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    response = client.responses.create(
        model="gpt-5.4-nano",
        instructions="Return only JSON that matches the provided schema.",
        input=prompt,
        text={
            "format": {
                "type": "json_schema",
                "name": name,
                "schema": schema,
                "strict": True,
            }
        },
    )
    return json.loads(response.output_text)


def extract_ticket(message: str):
    prompt = f"""
    Extract this support message into a ticket.
    Choose category and urgency from the allowed schema values.

    Message:
    {message}
    """

    print(prompt)

    return ask_json(prompt, TICKET_SCHEMA, name="support_ticket")


def main():
    message = (
        "Ananya says invoice INV-2044 was charged twice. Finance review is due "
        "today, so she needs confirmation before 4 PM."
    )
    try:
        ticket = extract_ticket(message)
    except (json.JSONDecodeError, ValueError) as exc:
        print(f"Extraction failed: {exc}")
        return

    print(json.dumps(ticket, indent=2))


if __name__ == "__main__":
    main()

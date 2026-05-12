"""Prompt Technique 5: Extract messy text into JSON.
Day 1, Session 2: Prompt Engineering
Learning Objective: Use a prompt to transform unstructured text into structured data.
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.common import ask_model


def main():
    messy_note = """
    Priya from Acme says the login page keeps spinning after she enters the OTP.
    She has a customer demo in 2 hours and wants support to check whether her
    account is locked. Email is priya@acme.test.
    """
    prompt = f"""
    Extract the support request as JSON with these keys:
    customer_name, company, issue, urgency, contact, requested_action.

    Text:
    {messy_note}
    """
    result = ask_model(prompt, max_output_tokens=300)
    print("Raw model output:")
    print(result)

    try:
        parsed = json.loads(result)
        print("\nParsed JSON:")
        print(json.dumps(parsed, indent=2))
    except json.JSONDecodeError:
        print("\nThe model did not return valid JSON. Day 2 will fix this with schemas.")


if __name__ == "__main__":
    main()

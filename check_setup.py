"""
============================================================
Vevolve AI Engineering Workshop — Setup Verification Script
============================================================
Run this after completing all setup steps:

    python check_setup.py

It will check every requirement and tell you exactly what
is working and what still needs to be fixed.
============================================================
"""

import sys
import subprocess

# ── Helpers ─────────────────────────────────────────────────

PASS = "  [PASS]"
FAIL = "  [FAIL]"
WARN = "  [WARN]"
INFO = "        "

def section(title):
    print(f"\n{'─' * 52}")
    print(f"  {title}")
    print(f"{'─' * 52}")

def ok(msg):
    print(f"{PASS} {msg}")

def fail(msg):
    print(f"{FAIL} {msg}")

def warn(msg):
    print(f"{WARN} {msg}")

def info(msg):
    print(f"{INFO} {msg}")


# ── Check 1: Python version ──────────────────────────────────

def check_python():
    section("1. Python Version")
    major, minor = sys.version_info.major, sys.version_info.minor
    version_str = f"{major}.{minor}.{sys.version_info.micro}"
    if major == 3 and minor >= 10:
        ok(f"Python {version_str} — good to go")
    else:
        fail(f"Python {version_str} found, but 3.10 or higher is required")
        info("Download the latest version from: https://www.python.org/downloads")
        return False
    return True


# ── Check 2: Required packages ──────────────────────────────

REQUIRED_PACKAGES = [
    ("openai",       "openai"),
    ("dotenv",       "python-dotenv"),
    ("chromadb",     "chromadb"),
    ("pypdf",        "pypdf"),
    ("crewai",       "crewai"),
    ("crewai_tools", "crewai-tools"),
    ("requests",     "requests"),
    ("rich",         "rich"),
]

def check_packages():
    section("2. Required Packages")
    all_ok = True
    for import_name, pip_name in REQUIRED_PACKAGES:
        try:
            __import__(import_name)
            ok(f"{pip_name}")
        except ImportError:
            fail(f"{pip_name} — not installed")
            info(f"Fix: pip install {pip_name}")
            all_ok = False
    return all_ok


# ── Check 3: .env file ──────────────────────────────────────

def check_env_file():
    section("3. .env File")
    import os
    if not os.path.exists(".env"):
        fail(".env file not found in current directory")
        info("Fix: copy .env.example to .env and fill in your keys")
        info("     cp .env.example .env   (Mac/Linux)")
        info("     copy .env.example .env  (Windows)")
        return False
    ok(".env file exists")
    return True


# ── Check 4: OpenAI API Key ──────────────────────────────────

def check_openai_key():
    section("4. OpenAI API Key")
    try:
        from dotenv import load_dotenv
        load_dotenv()
        import os
        key = os.getenv("OPENAI_API_KEY", "")

        if not key:
            fail("OPENAI_API_KEY is not set in your .env file")
            info("Fix: open .env and add:  OPENAI_API_KEY=your-key-here")
            return False

        if key == "your-openai-api-key-here":
            fail("OPENAI_API_KEY still has the placeholder value")
            info("Fix: replace 'your-openai-api-key-here' with the real key from Vevolve")
            return False

        if not key.startswith("sk-"):
            warn("OPENAI_API_KEY doesn't look like a standard OpenAI key (should start with sk-)")
            info("If Vevolve provided a custom key format this may still be fine")

        # Live test
        ok(f"OPENAI_API_KEY found (ends in ...{key[-4:]})")
        print(f"{INFO} Testing live connection to OpenAI...")

        import openai
        client = openai.OpenAI(api_key=key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Reply with exactly: SETUP OK"}],
            max_tokens=10
        )
        reply = response.choices[0].message.content.strip()
        ok(f"Live API call successful — model replied: \"{reply}\"")
        return True

    except openai.AuthenticationError:
        fail("OpenAI API key is invalid or expired")
        info("Contact Vevolve to get a valid key")
        return False
    except openai.RateLimitError:
        warn("Rate limit hit during test — but the key itself is valid")
        ok("OpenAI API key is working (rate limited right now, will be fine in class)")
        return True
    except Exception as e:
        fail(f"Unexpected error testing OpenAI key: {e}")
        return False


# ── Check 5: Serper API Key ──────────────────────────────────

def check_serper_key():
    section("5. Serper API Key  (required for Day 4)")
    try:
        from dotenv import load_dotenv
        load_dotenv()
        import os
        import requests

        key = os.getenv("SERPER_API_KEY", "")

        if not key:
            fail("SERPER_API_KEY is not set in your .env file")
            info("Fix: sign up free at https://serper.dev then add to .env:")
            info("     SERPER_API_KEY=your-key-here")
            return False

        if key == "your-serper-api-key-here":
            fail("SERPER_API_KEY still has the placeholder value")
            info("Fix: replace 'your-serper-api-key-here' with your real key from serper.dev")
            return False

        ok(f"SERPER_API_KEY found (ends in ...{key[-4:]})")
        print(f"{INFO} Testing live connection to Serper...")

        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": key, "Content-Type": "application/json"},
            json={"q": "OpenAI", "num": 1},
            timeout=10
        )

        if response.status_code == 200:
            ok("Live Serper search successful — web search is working")
            return True
        elif response.status_code == 401:
            fail("Serper API key is invalid")
            info("Check your key at: https://serper.dev/dashboard")
            return False
        else:
            warn(f"Unexpected response from Serper (status {response.status_code})")
            info("Your key may still work — contact the instructor if unsure")
            return False

    except requests.exceptions.Timeout:
        warn("Serper request timed out — check your internet connection")
        return False
    except Exception as e:
        fail(f"Unexpected error testing Serper key: {e}")
        return False


# ── Check 6: OpenAI models ──────────────────────────────────

def check_models():
    section("6. OpenAI Model Access")
    try:
        from dotenv import load_dotenv
        load_dotenv()
        import os, openai

        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))
        models_to_check = ["gpt-4o-mini", "gpt-4o", "text-embedding-3-small"]
        available = [m.id for m in client.models.list().data]

        all_ok = True
        for model in models_to_check:
            if model in available:
                ok(f"{model} — available")
            else:
                fail(f"{model} — not available on this key")
                info("Contact Vevolve — this model needs to be enabled on your API key")
                all_ok = False
        return all_ok

    except Exception as e:
        warn(f"Could not check model access: {e}")
        info("This check requires a valid OpenAI key (run check 4 first)")
        return False


# ── Summary ─────────────────────────────────────────────────

def print_summary(results):
    section("SUMMARY")
    labels = [
        "Python version",
        "Required packages",
        ".env file",
        "OpenAI API key",
        "Serper API key",
        "OpenAI model access",
    ]
    all_passed = True
    for label, passed in zip(labels, results):
        status = "PASS" if passed else "FAIL"
        symbol = "[PASS]" if passed else "[FAIL]"
        print(f"  {symbol}  {label}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("  All checks passed. You are ready for the workshop!")
    else:
        print("  Some checks failed. Fix the issues above and run this script again.")
        print("  If you are stuck, contact your coordinator at least 2 days before Day 1.")
    print()


# ── Main ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print()
    print("  Vevolve AI Engineering Workshop — Setup Verification")
    print(f"  Python {sys.version}")

    results = [
        check_python(),
        check_packages(),
        check_env_file(),
        check_openai_key(),
        check_serper_key(),
        check_models(),
    ]

    print_summary(results)
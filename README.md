# Vevolve AI Engineering Workshop

A 5-day hands-on workshop covering LLM fundamentals, prompt engineering, RAG, tool calling, and multi-agent systems using Python and the OpenAI API.

---

## Before You Begin

**Complete the full setup guide sent by your coordinator before Day 1.**
This README is a quick reference — the setup guide has step-by-step instructions with screenshots for every step below.

---

## Quick Setup

### 1. Clone this repo

```bash
git clone https://github.com/cybroque/vevolve-ai-workshop.git
cd vevolve-ai-workshop
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API keys

Copy the example env file and fill in your keys:

```bash
# Mac / Linux
cp .env.example .env

# Windows
copy .env.example .env
```

Then open `.env` in VS Code and replace the placeholders:

```
OPENAI_API_KEY=your-openai-api-key-here     ← provided by Vevolve
SERPER_API_KEY=your-serper-api-key-here     ← sign up free at serper.dev
```

### 4. Verify everything works

```bash
python check_setup.py
```

All 6 checks should pass. If any fail, the script will tell you exactly what to fix.

---

## What You Need

| Requirement | Where to get it |
|---|---|
| Python 3.10+ | [python.org/downloads](https://www.python.org/downloads) |
| VS Code | [code.visualstudio.com](https://code.visualstudio.com) |
| Git | [git-scm.com/downloads](https://git-scm.com/downloads) |
| OpenAI API key | Provided by Vevolve before Day 1 |
| Serper API key | Free at [serper.dev](https://serper.dev) |

---

## Workshop Structure

| Day | Topic |
|---|---|
| Day 1 | LLM Fundamentals & Prompt Engineering |
| Day 2 | Stateful AI, Structured Outputs & Debugging |
| Day 3 | Retrieval Augmented Generation (RAG) |
| Day 4 | Tool Calling & Multi-Agent Systems |
| Day 5 | Capstone — Multi-Agent Simulation |

Starter scripts for each day will be added to the `days/` folder as the workshop progresses.

---

## Repo Structure

```
vevolve-ai-workshop/
├── README.md               ← you are here
├── requirements.txt        ← install all dependencies
├── .env.example            ← copy this to .env and fill in your keys
├── .gitignore              ← keeps your .env file safe
├── check_setup.py          ← run this to verify your setup
└── days/
    ├── day1/               ← Day 1 starter scripts (added before Day 1)
    ├── day2/               ← Day 2 starter scripts (added before Day 2)
    ├── day3/               ← Day 3 starter scripts (added before Day 3)
    ├── day4/               ← Day 4 starter scripts (added before Day 4)
    └── day5/               ← Day 5 capstone starter (added before Day 5)
```

---

## Security

- **Never commit your `.env` file.** It is in `.gitignore` and will not be tracked by Git.
- **Never share your API keys** in chat, email, or on screen during the workshop.
- If you accidentally expose a key, rotate it immediately at [platform.openai.com](https://platform.openai.com) or [serper.dev](https://serper.dev).

---

## Need Help?

If any setup step fails, contact your workshop coordinator **at least 2 days before Day 1**.
Post in the workshop group chat for faster responses.
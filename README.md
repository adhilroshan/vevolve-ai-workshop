# AI Workshop

This workshop teaches participants how to build useful AI workflows in Python.
Each day has short concept demos and ends with a small project that participants
can run, modify, and show.

## Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill in your API settings:

```env
OPENAI_API_KEY=
OPENAI_BASE_URL=
OPENAI_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
```

`OPENAI_BASE_URL` is optional when using the official OpenAI endpoint. Set it
when using an OpenAI-compatible provider.

## Daily Outcomes

- **Day 1:** Build a prompt assistant for summarizing, rewriting, action items,
  and test-case generation.
- **Day 2:** Build a support ticket extractor that turns messy messages into
  validated JSON.
- **Day 3:** Build a RAG knowledge-base assistant with ingestion, retrieval,
  source citations, and a Streamlit UI.
- **Day 4:** Build a tool-using research assistant and compare plain pipelines
  with agent-style orchestration.

## Recommended Flow

Run the numbered session files first, then complete the daily project:

```bash
python day-1/project_prompt_assistant/main.py
python day-2/project_ticket_extractor/main.py
python day-3/project_rag_assistant/ingest.py
python day-3/project_rag_assistant/ask.py
python day-4/project_research_assistant/main.py
```

Streamlit apps are optional UI wrappers after the command-line projects work:

```bash
streamlit run day-2/project_ticket_extractor/app.py
streamlit run day-3/project_rag_assistant/app.py
streamlit run day-4/project_research_assistant/app.py
```

# Autonomous Quiz Agent — Backend Overview

A FastAPI backend that orchestrates a multi-step LLM pipeline to extract concepts from text, build a topic hierarchy, generate quiz questions, rank them by difficulty, and validate the distribution.

## Folder Structure

```
Autonomous_Quiz_Agent/
├── README.md
├── notes.txt
├── pytest.ini
├── requirements.txt
├── .env                      # Environment variables (local only; not committed)
├── agents/
│   ├── __init__.py
│   ├── graph.py              # LangGraph wiring: nodes + edges + router
│   ├── state.py              # Shared state definition across nodes
│   ├── extractors/
│   │   ├── __init__.py
│   │   └── concept_extractor.py
│   ├── generators/
│   │   ├── __init__.py
│   │   └── quiz_generator.py
│   ├── organizers/
│   │   ├── __init__.py
│   │   └── hierarchy_builder.py
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── extract_prompt.py
│   │   ├── hierarchy_prompt.py
│   │   ├── quiz_prompt.py
│   │   ├── rank_prompt.py
│   │   └── validate_prompt.py
│   ├── rankers/
│   │   ├── __init__.py
│   │   └── difficulty_ranker.py
│   └── validators/
│       ├── __init__.py
│       └── difficulty_validator.py
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app + router registration
│   ├── routes/
│   │   ├── __init__.py
│   │   └── quiz_routes.py    # /quiz/generate endpoint
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── quiz_schema.py    # Request/response Pydantic models
│   └── services/
│       ├── __init__.py
│       └── agent_service.py  # Entry to run graph + optional visualization
├── artifacts/
│   └── graphs/
│       └── quiz_agent_graph.md  # Mermaid diagram of the LangGraph
├── assets/
├── core/
│   ├── __init__.py
│   ├── config.py             # Env variables & constants
│   ├── exceptions.py         # Custom exception types
│   ├── graph_visualizer.py   # Save graph as Mermaid text
│   ├── llm_parser.py         # Robust JSON extraction from LLM output
│   ├── llm.py                # LLM client (LangChain Groq)
│   └── logger.py             # File + console logging
├── logs/
│   └── agent.log             # Rotating logs
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_graph.py
    └── test_validation.py
```

## Environment Variables (.env)
Place a `.env` file at the project root. Values below are the recommended defaults; do not include or share the API key value.

```env
# Required
GROQ_API_KEY=************************    # Provide your Groq API key (do not commit)

# Optional (with defaults)
GROQ_MODEL=llama-3.1-8b-instant          # Default model used by the backend
LLM_TEMPERATURE=0.3                      # Sampling temperature
LLM_MAX_TOKENS=2048                      # Response token cap
DEBUG=false                              # Set true for verbose logs
```

- `GROQ_API_KEY`: Required. Loaded at startup; backend exits if missing.
- `GROQ_MODEL`: Defaults to `llama-3.1-8b-instant`. Keep current with Groq deprecations.
- `LLM_TEMPERATURE`: Defaults to `0.3`.
- `LLM_MAX_TOKENS`: Defaults to `2048`.
- `DEBUG`: When `true`, enables debug-level logs.

## Backend Pipeline & Data Flow

1. Request enters FastAPI at `POST /quiz/generate` with:
   ```json
   { "text": "<raw course/topic text>" }
   ```
2. `app.services.agent_service.run_quiz_agent()` builds the LangGraph and, by default, saves a Mermaid diagram to `artifacts/graphs/quiz_agent_graph.md`.
3. The graph executes with shared `QuizState`:
   - `extract` → `agents.extractors.concept_extractor`
     - Prompt: `EXTRACT_PROMPT`
     - Output: `concepts: List[{ name, description }]`
   - `organize` → `agents.organizers.hierarchy_builder`
     - Prompt: `HIERARCHY_PROMPT`
     - Output: `hierarchy: Topic → Subtopic → Concepts`
   - `generate` → `agents.generators.quiz_generator`
     - Prompt: `QUIZ_PROMPT`
     - Output: `questions: List[{ question, related_concept }]` (exactly 10)
   - `rank` → `agents.rankers.difficulty_ranker`
     - Prompt: `RANK_PROMPT`
     - Output: `ranked_questions: List[{ question, difficulty }]`
   - `validate` → `agents.validators.difficulty_validator`
     - Prompt: `VALIDATE_PROMPT`
     - Output: `{ validation_passed: bool, feedback: string }`
4. Conditional routing:
   - If `validation_passed: true` → `END`.
   - Else → re-route to `rank` (retry) until either validation passes or `MAX_RETRIES` (3) is reached.
5. Final response aggregates the last state:
   ```json
   {
     "concepts": [...],
     "hierarchy": {...},
     "questions": [...],
     "ranked_questions": [...],
     "validation_passed": true|false,
     "validation_feedback": "<optional>"
   }
   ```

## API
- `POST /quiz/generate`
  - Request: `{ text: string }`
  - Response: see final state aggregate above (`QuizResponse`).

## Running Locally (Windows)

1. Create and activate venv (optional if already present):
   ```powershell
   py -m venv .\venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Add `.env` with your `GROQ_API_KEY` and optional settings.
4. Start the API:
   ```powershell
   uvicorn app.main:app --reload --port 8000
   ```
5. Test the endpoint:
   ```powershell
   curl -X POST http://localhost:8000/quiz/generate -H "Content-Type: application/json" -d '{"text": "Explain Newton\'s laws of motion"}'
   ```

## Notes
- Mermaid graph is saved to `artifacts/graphs/quiz_agent_graph.md` for quick visualization.
- Logs are rotated in `logs/agent.log`. Set `DEBUG=true` for detailed trace.
- Ensure the selected `GROQ_MODEL` is supported; deprecated models will error.

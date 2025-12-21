# Autonomous Quiz Agent — Backend Overview

A FastAPI backend that orchestrates a multi-step LLM pipeline to extract concepts from text, build a topic hierarchy, generate quiz questions, rank them by difficulty, and validate the distribution.

## Folder Structure

```
Autonomous_Quiz_Agent/
├── README.md
├── notes.txt
├── pytest.ini
├── requirements.txt
├── .env                          # Backend environment variables (local only; not committed)
├── agents/
│   ├── __init__.py
│   ├── graph.py                  # LangGraph wiring: nodes + edges + router
│   ├── state.py                  # Shared state definition across nodes
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
│   ├── main.py                   # FastAPI app + router registration
│   ├── routes/
│   │   ├── __init__.py
│   │   └── quiz_routes.py        # /quiz/generate endpoint
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── quiz_schema.py        # Request/response Pydantic models
│   └── services/
│       ├── __init__.py
│       └── agent_service.py      # Entry to run graph + optional visualization
├── artifacts/
│   └── graphs/
│       └── quiz_agent_graph.md   # Mermaid diagram of the LangGraph
├── assets/
├── core/
│   ├── __init__.py
│   ├── config.py                 # Env variables & constants
│   ├── exceptions.py             # Custom exception types
│   ├── graph_visualizer.py       # Save graph as Mermaid text
│   ├── llm_parser.py             # Robust JSON extraction from LLM output
│   ├── llm.py                    # LLM client (LangChain Groq)
│   └── logger.py                 # File + console logging
├── frontend/                      # Next.js/React frontend
│   ├── package.json              # Frontend dependencies
│   ├── .env.local                # Frontend env (not committed)
│   ├── .next/
│   ├── app/                       # Next.js app directory
│   ├── components/               # React components
│   ├── hooks/                    # Custom React hooks
│   ├── lib/                      # Utility functions
│   ├── public/                   # Static assets
│   ├── styles/                   # CSS/styling
│   ├── next.config.mjs           # Next.js configuration
│   ├── tsconfig.json             # TypeScript configuration
│   └── node_modules/
├── logs/
│   └── agent.log                 # Rotating logs
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_graph.py
    └── test_validation.py
```

## Environment Variables

### Backend (.env at project root)
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

### Frontend (.env.local at frontend/ root)
Place a `.env.local` file in the `frontend/` directory. This is not committed.

```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

- `NEXT_PUBLIC_API_BASE_URL`: Backend API URL the frontend connects to. Change if running backend on a different port/host.

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
  - Response: see final state aggregate below (`QuizResponse`).

## Tech Stack

- **Backend**: Python 3.13+, FastAPI, LangChain, LangGraph, Groq LLM, Pydantic
- **Frontend**: Next.js 16+, React, TypeScript, Tailwind CSS, Radix UI
- **LLM**: Groq (llama-3.1-8b-instant)

## Running Locally (Windows)

### 1. Backend Setup

1. Create and activate venv (optional if already present):
   ```powershell
   py -m venv .\venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Add `.env` at project root with your `GROQ_API_KEY` and optional settings (see [Backend (.env at project root)](#backend-env-at-project-root)).

4. Start the backend API (default port 8000):
   ```powershell
   uvicorn app.main:app --reload --port 8000
   ```
   - Backend is now accessible at `http://localhost:8000`.
   - API docs available at `http://localhost:8000/docs`.

### 2. Frontend Setup

1. Navigate to frontend directory:
   ```powershell
   cd frontend
   ```

2. Install dependencies:
   ```powershell
   npm install
   # or
   pnpm install
   ```

3. Add `.env.local` at `frontend/` root (see [Frontend (.env.local at frontend/ root)](#frontend-env-local-at-frontend-root)):
   ```env
   NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
   ```

4. Start the frontend development server (default port 3000):
   ```powershell
   npm run dev
   # or
   pnpm dev
   ```
   - Frontend is now accessible at `http://localhost:3000`.

### 3. Testing the Full Stack

1. Ensure both backend (port 8000) and frontend (port 3000) are running.
2. Open `http://localhost:3000` in your browser.
3. Submit text to generate a quiz—the frontend will call the backend API.

### Optional: Build Frontend for Production

```powershell
cd frontend
npm run build
npm run start
```

## Notes
- Mermaid graph is saved to `artifacts/graphs/quiz_agent_graph.md` for quick visualization of the backend pipeline.
- Logs are rotated in `logs/agent.log`. Set `DEBUG=true` in `.env` for detailed trace.
- Ensure the selected `GROQ_MODEL` is supported; deprecated models will error.
- Frontend connects to the backend API via `NEXT_PUBLIC_API_BASE_URL` env variable. Update it if running on a different host/port.
- Both backend and frontend must be running for the full stack to work.

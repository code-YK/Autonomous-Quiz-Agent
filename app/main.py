from fastapi import FastAPI
from app.routes.quiz_routes import router as quiz_router
from starlette.middleware.cors import CORSMiddleware

# Ensure GROQ_API_KEY is loaded at startup
from core.config import GROQ_API_KEY
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not loaded at startup")

# FastAPI app instance
app = FastAPI(title="Autonomous Quiz Agent")

# CORS CONFIG (ADD THIS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite / React
        "http://localhost:3000",  # fallback
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API is running"}

app.include_router(quiz_router, prefix="/quiz")

@app.get("/health")
def health():
    return {"status": "ok"}

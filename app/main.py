from fastapi import FastAPI
from app.routes.quiz_routes import router as quiz_router

# Ensure GROQ_API_KEY is loaded at startup
from core.config import GROQ_API_KEY
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not loaded at startup")

# FastAPI app instance
app = FastAPI(title="Autonomous Quiz Agent")

@app.get("/")
def root():
    return {"status": "API is running"}

app.include_router(quiz_router, prefix="/quiz")


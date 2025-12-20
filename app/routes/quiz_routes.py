from fastapi import APIRouter, HTTPException
from app.schemas.quiz_schema import QuizRequest, QuizResponse
from app.services.agent_service import run_quiz_agent

router = APIRouter(tags=["Quiz Agent"])

@router.post("/generate", response_model=QuizResponse)
def generate_quiz(payload: QuizRequest):
    try:
        result = run_quiz_agent(payload.text)
        return result

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal error while generating quiz"
        )
from pydantic import BaseModel
from typing import List, Dict, Any


class QuizRequest(BaseModel):
    text: str


class QuizResponse(BaseModel):
    concepts: Any
    hierarchy: Any
    questions: List[Dict]
    ranked_questions: List[Dict]
    validation_passed: bool
    validation_feedback: str | None = None

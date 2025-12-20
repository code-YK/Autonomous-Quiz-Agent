from typing import TypedDict, List, Dict, Any

class QuizState(TypedDict, total=False):
    # Input
    raw_text: str

    # Intermediate
    chunks: List[str]
    concepts: List[Dict[str, Any]]
    hierarchy: Dict[str, Any]

    # Quiz
    questions: List[Dict[str, Any]]
    ranked_questions: List[Dict[str, Any]]

    # Validation
    validation_passed: bool
    validation_feedback: str

    # Retry count
    retry_count: int

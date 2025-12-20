from agents.prompts import RANK_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger

logger = get_logger(__name__)


def difficulty_ranker(state):
    logger.info("Assigning difficulty levels")

    questions = state["questions"]

    response = invoke_llm(
        RANK_PROMPT.format(questions=questions)
    )

    logger.info("Difficulty ranking completed")

    return {
        "ranked_questions": response
    }

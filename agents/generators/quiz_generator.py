from agents.prompts import QUIZ_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger

logger = get_logger(__name__)


def quiz_generator(state):
    logger.info("Generating quiz questions")

    hierarchy = state["hierarchy"]

    response = invoke_llm(
        QUIZ_PROMPT.format(hierarchy=hierarchy)
    )

    logger.info("Quiz generation completed")

    return {
        "questions": response
    }

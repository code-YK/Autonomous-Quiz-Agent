from agents.prompts import QUIZ_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger
from core.llm_parser import extract_json

logger = get_logger(__name__)


def quiz_generator(state):
    logger.info("Generating quiz questions")

    hierarchy = state["hierarchy"]

    raw_response = invoke_llm(
        QUIZ_PROMPT.format(hierarchy=hierarchy)
    )

    # parse response as JSON
    try:
        response = extract_json(raw_response)
    except Exception as e:
        logger.warning("Quiz generation failed: %s", e)
        return {"questions": []}
    
    logger.info("Quiz generation completed")

    return {
        "questions": response
    }

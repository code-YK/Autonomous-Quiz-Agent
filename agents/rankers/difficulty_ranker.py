from agents.prompts import RANK_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger
from core.llm_parser import extract_json

logger = get_logger(__name__)


def difficulty_ranker(state):
    logger.info("Assigning difficulty levels")

    questions = state["questions"]

    raw_response = invoke_llm(
        RANK_PROMPT.format(questions=questions)
    )

    # parse response as JSON
    try:
        response = extract_json(raw_response)
    except Exception as e:
        logger.warning("Difficulty ranking failed: %s", e)
        return {"ranked_questions": []}

    logger.info("Difficulty ranking completed")

    return {
        "ranked_questions": response
    }

from agents.prompts import HIERARCHY_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger
from core.llm_parser import extract_json

logger = get_logger(__name__)


def hierarchy_builder(state):
    logger.info("Building concept hierarchy")

    concepts = state["concepts"]

    raw_response = invoke_llm(
        HIERARCHY_PROMPT.format(concepts=concepts)
    )

    # parse response as JSON
    try:
        response = extract_json(raw_response)
    except Exception as e:
        logger.warning("Hierarchy building failed: %s", e)
        return {"hierarchy": []}

    logger.info("Hierarchy built successfully")

    return {
        "hierarchy": response
    }

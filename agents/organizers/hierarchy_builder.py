from agents.prompts import HIERARCHY_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger

logger = get_logger(__name__)


def hierarchy_builder(state):
    logger.info("Building concept hierarchy")

    concepts = state["concepts"]

    response = invoke_llm(
        HIERARCHY_PROMPT.format(concepts=concepts)
    )

    logger.info("Hierarchy built successfully")

    return {
        "hierarchy": response
    }

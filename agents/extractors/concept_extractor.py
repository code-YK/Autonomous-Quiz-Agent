from agents.prompts import EXTRACT_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger

logger = get_logger(__name__)


def concept_extractor(state):
    logger.info("Starting concept extraction")

    raw_text = state["raw_text"]

    response = invoke_llm(
        EXTRACT_PROMPT.format(chunk=raw_text)
    )

    logger.info("Concept extraction completed")

    return {
        "concepts": response
    }

from agents.prompts import EXTRACT_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger
from core.llm_parser import extract_json

logger = get_logger(__name__)


def concept_extractor(state):
    logger.info("Starting concept extraction")

    raw_text = state["raw_text"]

    raw_response = invoke_llm(
        EXTRACT_PROMPT.format(chunk=raw_text)
    )

    # parse response as JSON
    try:
        response = extract_json(raw_response)
    except Exception as e:
        logger.warning("Concept extraction parse failed: %s", e)
        return {"concepts": []}
    
    logger.info("Concept extraction completed")

    return {
        "concepts": response
    }

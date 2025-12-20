import json
from agents.prompts import VALIDATE_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger
from core.llm_parser import extract_json, LLMParseError

logger = get_logger(__name__)


def difficulty_validator(state):
    logger.info("Validating difficulty logic")

    ranked_questions = state["ranked_questions"]

    try:
        raw_response = invoke_llm(
            VALIDATE_PROMPT.format(ranked_questions=ranked_questions)
        )

        response = extract_json(raw_response)

        if not isinstance(response, dict):
            raise ValueError("Validator response is not a JSON object")

    except (LLMParseError, ValueError) as e:
        logger.warning("Validator output invalid: %s", str(e))
        return {
            "validation_passed": False,
            "validation_feedback": "Invalid validator response format",
            "retry_count": state.get("retry_count", 0) + 1
        }

    validation_passed = response.get(
        "validation_passed",
        response.get("valid", False)  # fallback if model uses "valid"
    )

    feedback = response.get(
        "feedback",
        response.get("reason", "")
    )


    if validation_passed:
        logger.info("Difficulty validation PASSED")
    else:
        logger.warning("Difficulty validation FAILED: %s", feedback)

    retry_count = state.get("retry_count", 0) + 1

    return {
        "validation_passed": validation_passed,
        "validation_feedback": feedback,
        "retry_count": retry_count
    }

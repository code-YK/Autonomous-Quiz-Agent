import json
from agents.prompts.validate_prompt import VALIDATE_PROMPT
from core.llm import invoke_llm
from core.logger import get_logger

logger = get_logger(__name__)


def difficulty_validator(state):
    logger.info("Validating difficulty logic")

    ranked_questions = state["ranked_questions"]

    raw_response = invoke_llm(
        VALIDATE_PROMPT.format(ranked_questions=ranked_questions)
    )

    # SAFETY: Parse response as JSON
    if isinstance(raw_response, str):
        try:
            response = json.loads(raw_response)
        except json.JSONDecodeError:
            logger.warning("Validation response not JSON. Failing validation.")
            return {
                "validation_passed": False,
                "validation_feedback": "Invalid response format from validator"
            }
    else:
        response = raw_response

    validation_passed = response.get("validation_passed", False)
    feedback = response.get("feedback", "")

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

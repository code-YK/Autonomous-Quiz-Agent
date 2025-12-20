from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from core.config import (
    GROQ_API_KEY,
    DEFAULT_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
)
from core.logger import get_logger
from core.exceptions import LLMInvocationError

logger = get_logger(__name__)


def _validate_env():
    if not GROQ_API_KEY:
        raise EnvironmentError(
            "GROQ_API_KEY not found. Please set it in your .env file."
        )


_validate_env()


# LLM INSTANCE (SINGLETON)
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model=DEFAULT_MODEL,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
)


def invoke_llm(prompt: str):
    """
    Standardized LLM invocation.
    Always returns parsed content (string / JSON).
    """

    logger.debug(f"GROQ_API_KEY present: {bool(GROQ_API_KEY)}")

    try:
        logger.debug("Invoking LLM...")
        response = llm.invoke([HumanMessage(content=prompt)])

        logger.debug("LLM response received.")
        return response.content

    except Exception as e:
        logger.exception("LLM invocation failed")
        raise LLMInvocationError(str(e))

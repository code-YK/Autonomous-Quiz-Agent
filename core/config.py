import os
from dotenv import load_dotenv

load_dotenv()

# LLM CONFIGURATION
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DEFAULT_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.1-70b-versatile"
)

TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.3))
MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", 2048))


# VALIDATION RULES
EASY_COUNT = 3
MEDIUM_COUNT = 4
HARD_COUNT = 3
TOTAL_QUESTIONS = 10


# APP SETTINGS
APP_NAME = "Autonomous Quiz Agent"
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

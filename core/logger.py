import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler
from pathlib import Path
from core.config import DEBUG

# LOG CONFIG
LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "agent.log"

# Ensure logs directory exists
LOG_DIR.mkdir(exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(LOG_LEVEL)

    # File Handler (Persistent Logs)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(LOG_LEVEL)
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    # Console Handler (Pretty Logs)
    console_handler = RichHandler(
        rich_tracebacks=True,
        show_time=False,
        show_level=True,
        show_path=False,
    )
    console_handler.setLevel(LOG_LEVEL)

    # Attach Handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

import logging
import os

def get_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("trading_bot")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        handler = logging.FileHandler("logs/bot.log")
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
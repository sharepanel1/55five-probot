import logging
import os
import time
from telegram import Bot
from config.settings import Settings

settings = Settings()
logger = logging.getLogger(__name__)

class ErrorHandler:
    def __init__(self):
        self.bot = Bot(token=settings.TELEGRAM_TOKEN)
        self.max_retries = 5

    def handle(self, func):
        def wrapper(*args, **kwargs):
            for attempt in range(self.max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    self._process_error(e, attempt)
            self._emergency_restart()
        return wrapper

    def _process_error(self, error, attempt):
        logger.error(f"Attempt {attempt+1} failed: {str(error)}")
        time.sleep(2 ** attempt)
        if attempt == self.max_retries - 1:
            self.bot.send_message(
                chat_id=settings.CHAT_ID,
                text=f"🚨 Gagal setelah {self.max_retries} percobaan: {str(error)}"
            )

    def _emergency_restart(self):
        os.system("docker-compose down && docker-compose up -d")

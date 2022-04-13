import logging
import os

import requests

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s <%(name)s> [%(levelname)s] %(message)s',
)

logger = logging.getLogger("bot")

def send_message(chat_id: str, text: str) -> None:
  token = os.environ.get("TELEGRAM_BOT_TOKEN")
  url = f"https://api.telegram.org/bot{token}/sendMessage"
  payload = {
    "chat_id": chat_id,
    "text": text,
  }

  requests.get(url, params=payload)

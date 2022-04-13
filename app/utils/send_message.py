import os

import requests

def send_message(chat_id: str, text: str) -> None:
  token = os.environ.get("TELEGRAM_BOT_TOKEN")
  url = f"https://api.telegram.org/bot{token}/sendMessage"
  payload = {
    "chat_id": chat_id,
    "text": text,
  }

  requests.get(url, params=payload)

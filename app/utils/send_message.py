import os

import requests
from telegram import Bot

def send_message(bot: Bot, chat_id: str, text: str) -> None:
  url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
  payload = {
    "chat_id": chat_id,
    "text": text,
  }

  requests.get(url, params=payload)

import os

from telegram import Bot

from .utils import log

try:
  token = os.environ.get("TELEGRAM_BOT_TOKEN")

  if token is None:
    raise Exception("Missing bot token")

  bot = Bot(token)

  log.info("Starting bot... %s", "OK")
except Exception as exc:
  bot = None

  log.exception("Starting bot... %s: %s", "ERR", exc)

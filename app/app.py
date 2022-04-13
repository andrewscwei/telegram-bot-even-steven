import http
import os

import telegram
from flask import Flask, Response, request

from .bot import bot
from .commands import marco_polo
from .utils import log

app = Flask(__name__)

@app.get("/health")
def health_check() -> Response:
  return "OK", http.HTTPStatus.OK

@app.get("/version")
def version() -> Response:
  return os.getenv("BUILD_NUMBER", "0"), http.HTTPStatus.OK

@app.post("/")
def index() -> Response:
  if bot is None:
    return "Bot is inactive", http.HTTPStatus.INTERNAL_SERVER_ERROR

  try:
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text.encode('utf-8').decode()

    log.info("Parsing incoming message... %s: %s", "OK", update)

    if text.lower() == "marco":
      marco_polo(bot, chat_id)
  except Exception as exc:
    log.exception("Parsing incoming message... %s: %s", "ERR", exc)

  return "", http.HTTPStatus.NO_CONTENT

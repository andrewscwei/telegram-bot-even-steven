import http
import os

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
    data = request.get_json()
    chat_id: str = data["message"]["chat"]["id"]
    text: str = data["message"]["text"]

    log.info("Parsing message payload... %s: %s", "OK", data)

    if text.lower() == "marco":
      marco_polo(bot, chat_id)
  except Exception as exc:
    log.exception("Parsing message payload... %s: %s", "ERR", exc)

  return "", http.HTTPStatus.NO_CONTENT

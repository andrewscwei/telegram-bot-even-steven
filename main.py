import http
import os

import requests
import telegram
from flask import Flask, Response, request

from app.bot import setup_bot
from app.db import setup_db, test_db

app = Flask(__name__)
db = setup_db(app)
dispatcher = setup_bot()

@app.get("/health")
def health_check() -> Response:
  return {
    "bot": "up" if dispatcher is not None else "down",
    "build": os.environ.get("BUILD_NUMBER"),
    "db": "up" if test_db(db) else "down",
  }, http.HTTPStatus.OK

@app.get("/info")
def info() -> Response:
  return requests.get(f"https://api.telegram.org/bot{dispatcher.bot.token}/getMe").content

@app.get("/rebase")
def reset() -> Response:
  rebase_url = os.environ.get("REBASE_URL")

  if rebase_url is None:
    return { "error": "No rebase URL provided" }, http.HTTPStatus.INTERNAL_SERVER_ERROR

  return requests.get(f"https://api.telegram.org/bot{dispatcher.bot.token}/setWebhook?url={rebase_url}").content

@app.post("/")
def index() -> Response:
  if dispatcher is None:
    return "Bot is inactive", http.HTTPStatus.INTERNAL_SERVER_ERROR

  update = telegram.Update.de_json(request.get_json(force=True), dispatcher.bot)
  dispatcher.process_update(update)

  return "", http.HTTPStatus.NO_CONTENT

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=os.environ.get("PORT"))

import http
import os

import requests
import telegram
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy

from app.bot import setup_bot

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.environ.get('DATABASE_URL')}"
db = SQLAlchemy(app)
token = os.environ.get("BOT_TOKEN")
dispatcher = setup_bot(token)

@app.get("/health")
def health_check() -> Response:
  return "OK", http.HTTPStatus.OK

@app.get("/version")
def version() -> Response:
  return os.getenv("BUILD_NUMBER", "0"), http.HTTPStatus.OK

@app.get("/rebase")
def reset() -> Response:
  return requests.get(f"https://api.telegram.org/bot{token}/setWebhook\?url=https://telegram-bot-even-steven.herokuapp.com").content

@app.post("/")
def index() -> Response:
  if dispatcher is None:
    return "Bot is inactive", http.HTTPStatus.INTERNAL_SERVER_ERROR

  update = telegram.Update.de_json(request.get_json(force=True), dispatcher.bot)
  dispatcher.process_update(update)

  return "", http.HTTPStatus.NO_CONTENT

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=os.environ.get("PORT"))

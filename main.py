import http
import os

from dotenv import load_dotenv
from flask import Flask, request
from telegram.ext import Updater
from werkzeug import Response

from app.commands import marco_polo
from app.utils import log, send_message

load_dotenv()

app = Flask(__name__)
updater = Updater(token=os.environ.get("TELEGRAM_BOT_TOKEN"))
dispatcher = updater.dispatcher

@app.get("/health")
def health_check() -> Response:
  return "OK", http.HTTPStatus.OK

@app.get("/version")
def version() -> Response:
  return os.getenv("BUILD_NUMBER", "0"), http.HTTPStatus.OK

@app.post("/")
def index() -> Response:
  data = request.get_json()

  log.info(f"Receiving payload... OK: {data}")

  chat_id = data["message"]["chat"]["id"]
  text: str = data["message"]["text"]

  if text.lower() == "marco":
    marco_polo(chat_id)

  return "", http.HTTPStatus.NO_CONTENT

if __name__ == "__main__":
  app.run()

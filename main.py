"""
App entrypoint.
"""

import http
import logging
import os

from dotenv import load_dotenv
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CallbackContext, Dispatcher, Filters, MessageHandler
from werkzeug import Response

load_dotenv()
logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

def echo(update: Update, context: CallbackContext) -> None:
  update.message.reply_text(update.message.text)

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))

dispatcher = Dispatcher(bot=bot, update_queue=None)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

@app.get("/health")
def health_check() -> Response:
  return "OK", http.HTTPStatus.OK

@app.get("/version")
def version() -> Response:
  return os.getenv("BUILD_NUMBER", "0"), http.HTTPStatus.OK

@app.post("/")
def index() -> Response:
  dispatcher.process_update(Update.de_json(request.get_json(force=True), bot))
  return "", http.HTTPStatus.NO_CONTENT

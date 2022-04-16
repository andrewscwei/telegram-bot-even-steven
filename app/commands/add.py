from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense


def add(update: Update, context: CallbackContext):
  expense = Expense(chat_id=update.message.chat_id, user="asdf", amount=100, label="Hello, world!")
  db.session.add(expense)
  db.session.commit()

  update.message.reply_text('OK')

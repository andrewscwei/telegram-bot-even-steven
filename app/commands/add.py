from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Transaction


def add(update: Update, context: CallbackContext):
  tx = Transaction(chat_id=update.message.chat_id)
  db.session.add(tx)
  db.session.commit()

  update.message.reply_text('OK')

from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import log


def reset(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id

  try:
    deleted = Expense.query.filter_by(chat_id=chat_id).delete()
    db.session.commit()
    update.message.reply_text('Done, reset all expenses.')
  except Exception as exc:
    log.exception('Resetting expenses for chat ID %s... %s: %s', chat_id, 'ERR', exc)
    db.session.rollback()
    update.message.reply_text('Oops! There seems to be an error resetting all expenses, please try again later.')

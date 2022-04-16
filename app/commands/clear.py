from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import log
from .show import show


def clear(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id

  try:
    expenses = Expense.query.filter_by(chat_id=chat_id)

    if expenses.count() < 1:
      update.message.reply_text(
        'Nothing to clear 🙃',
        parse_mode=ParseMode.MARKDOWN,
        quote=False,
      )
    else:
      show(update, context)
      expenses.delete()
      db.session.commit()
      update.message.reply_text(
        '👌 All expenses are cleared',
        parse_mode=ParseMode.MARKDOWN,
        quote=False,
      )
  except Exception as exc:
    log.exception('Resetting expenses for chat ID %s... %s: %s', chat_id, 'ERR', exc)
    db.session.rollback()
    update.message.reply_text(
      '💩 Something went wrong, please try again later',
      parse_mode=ParseMode.MARKDOWN,
      quote=False,
    )

from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import log


def add(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  user = update.message.from_user.username

  try:
    amount = float(context.args[0])
  except Exception as exc:
    log.exception('Parsing amount... %s: %s', 'ERR', exc)
    return update.message.reply_text('Oops! Looks like you didn\'t provide a valid amount, please try again (correct format: /add 99.99 <optional_label>).')

  label = ' '.join(context.args[1:])

  expense = Expense(chat_id=chat_id, user=user, amount=amount, label=label)

  db.session.add(expense)
  db.session.commit()

  update.message.reply_text(f'Done! Added ${amount} for @{user}')

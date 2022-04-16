from telegram import Update
from telegram.ext import CallbackContext

from ..models import Expense
from ..utils import log


def show(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id

  try:
    expenses = Expense.query.filter_by(chat_id=chat_id)
    reply = 'Here is the current standing of expenses:'
    reply += '\n\n'

    for expense in expenses:
      reply += f'@{expense.user}: {expense.amount}\n'

    update.message.reply_text(reply)

  except Exception as exc:
    log.exception('Showing current expenses for chat ID %s... %s: %s', chat_id, 'ERR', exc)
    update.message.reply_text('Oops! Something went wrong, please try again later.')

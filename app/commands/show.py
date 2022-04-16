from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..models import Expense
from ..utils import format_currency


def show(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  expenses = Expense.query.filter_by(chat_id=chat_id)

  if expenses.count() < 1:
    reply = 'Nothing to show 🙃'
  else:
    reply = 'Current expenses 👇'
    reply += '\n'

    for expense in expenses:
      reply += '\n'
      reply += f'@{expense.user} {format_currency(expense.amount)}'

      if expense.label.strip():
        reply += f': {expense.label}'

  update.message.reply_text(
    reply,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

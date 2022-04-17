from flask_sqlalchemy import BaseQuery
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
    reply += '\n\n'
    reply += format_expenses(expenses)

  update.message.reply_text(
    reply,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

def format_expenses(expenses: BaseQuery):
  reply = ''

  for expense in expenses:
    reply += '\n'
    reply += f'<`{expense.id}`> @{expense.user} `{format_currency(expense.amount)}`'

    if expense.label.strip():
      reply += f': {expense.label}'

  if reply.startswith('\n'):
    reply = reply.removeprefix('\n')

  return reply

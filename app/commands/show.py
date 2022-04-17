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
    total = sum(expense.amount for expense in expenses)
    reply = f'Total expenses: `{format_currency(total)}`, breakdown 👇'
    reply += '\n\n'
    reply += format_expenses(expenses)

  update.message.reply_text(
    reply,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

def format_expenses(expenses: BaseQuery):
  ret = ''

  for expense in expenses:
    ret += '\n'
    ret += f'<`{expense.id}`> @{expense.user} `{format_currency(expense.amount)}`'

    if expense.label.strip():
      ret += f': {expense.label}'

  if ret.startswith('\n'):
    ret = ret.removeprefix('\n')

  return ret

from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import format_currency


def balances(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  reply = ''

  expenses_by_user = db.session.query(Expense.user, db.func.sum(Expense.amount)).filter_by(chat_id=chat_id).group_by(Expense.user).all()
  num_user = len(expenses_by_user)

  if num_user < 1:
    reply = 'Nothing to show 🙃'
  else:
    reply += 'Outstanding balances 👇'
    reply += '\n\n'
    reply += format_balances(expenses_by_user)

  update.message.reply_text(
    reply,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

def format_balances(expenses_by_user) -> str:
  total = sum(amount for user, amount in expenses_by_user)
  total_per_user = total / len(expenses_by_user)

  ret = ''

  for (user, amount) in expenses_by_user:
    ret += '\n'
    ret += f'@{user}: `{format_currency(amount - total_per_user)}`'

  if ret.startswith('\n'):
    ret = ret.removeprefix('\n')

  return ret

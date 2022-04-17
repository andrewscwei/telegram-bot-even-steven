from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import format_currency


def balances(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  reply = ''

  expenses_by_user = db.session.query(Expense.user, db.func.sum(Expense.amount)).filter_by(chat_id=chat_id).group_by(Expense.user).all()
  balances_by_user = compute_balances(expenses_by_user)

  if len(balances_by_user) < 1:
    reply = 'No outstanding balances 🙃'
  elif is_even_steven(balances_by_user):
    reply = 'No one owes anyone anything, even-steven 😎'
  else:
    reply += 'Outstanding balances 👇'
    reply += '\n\n'
    reply += format_balances(balances_by_user)

  update.message.reply_markdown(
    reply,
    quote=False,
  )

def compute_balances(expenses_by_user: list[tuple[str, float]]) -> tuple[str, float]:
  total_expenses = sum(amount for user, amount in expenses_by_user)
  owing_per_user = total_expenses / len(expenses_by_user)

  return list(map(lambda t: (t[0], t[1] - owing_per_user), expenses_by_user))

def is_even_steven(balances_by_user: list[tuple[str, float]]) -> bool:
  for (user, amount) in balances_by_user:
    if amount != 0:
      return False

  return True

def format_balances(balances_by_user: list[tuple[str, float]]) -> str:
  ret = ''

  for (user, amount) in balances_by_user:
    ret += '\n'
    ret += f'@{user}: `{format_currency(amount)}`'

  ret = ret.lstrip('\n')

  return ret

from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import format_currency


def balances(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  reply = ''

  balances_by_user = compute_balances(chat_id)

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

def compute_expenses(chat_id: str) -> tuple[str, str, float]:
  expenses_by_user = db.session.query(
    Expense.user_id,
    db.func.max(Expense.user_alias),
    db.func.sum(Expense.amount),
  ) \
    .filter_by(chat_id=chat_id) \
    .group_by(Expense.user_id) \
    .all()

  return expenses_by_user

def compute_balances(chat_id: str) -> tuple[str, str, float]:
  expenses_by_user = compute_expenses(chat_id)
  num_users = len(expenses_by_user)

  if num_users <= 0:
    return []

  total_expenses = sum(amount for user_id, user_alias, amount in expenses_by_user)
  owing_per_user = total_expenses / num_users

  return list(map(lambda t: (t[0], t[1], t[2] - owing_per_user), expenses_by_user))

def is_even_steven(balances_by_user: list[tuple[str, str, float]]) -> bool:
  for (user_id, user_alias, amount) in balances_by_user:
    if amount != 0:
      return False

  return True

def format_balances(balances_by_user: list[tuple[str, str, float]]) -> str:
  ret = ''

  for (user_id, user_alias, amount) in balances_by_user:
    ret += '\n'
    ret += f'{user_alias}: `{format_currency(amount)}`'

  ret = ret.lstrip('\n')

  return ret

from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import format_currency, parse_int


def remove(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  user_id = update.message.from_user.id

  try:
    idx = parse_int(context.args[0])
  except Exception as exc:
    raise Exception('💩 Looks like you didn\'t provide a valid expense ID (example: `/remove <expense_id>`)') from exc

  expenses = Expense.query.filter_by(chat_id=chat_id)
  num_expenses = expenses.count()
  expense = expenses[idx - 1] if num_expenses >= idx else None

  if expense is None:
    return update.message.reply_markdown(
      f'✋ No expense found with ID {idx}',
      quote=False,
    )

  reply = ''

  if expense.user_id == user_id:
    reply = f'👌 Removed expense for {expense.user_alias} {format_currency(expense.amount)}'

    if expense.label.strip():
      reply += f': {expense.label}'

    try:
      db.session.delete(expense)
      db.session.commit()
    except Exception as exc:
      db.session.rollback()
      raise exc
  else:
    reply = f'✋ You can\'t remove someone else\'s expense, have {expense.user_alias} do it instead'

  update.message.reply_markdown(
    reply,
    quote=False,
  )

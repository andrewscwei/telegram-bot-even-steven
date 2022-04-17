from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import format_currency, parse_int


def remove(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id

  try:
    expense_id = parse_int(context.args[0])
  except Exception as exc:
    raise Exception('💩 Looks like you didn\'t provide a valid expense ID (example: `/remove <expense_id>`)') from exc

  expense = Expense.query.filter_by(id=expense_id, chat_id=chat_id).first()

  if expense is None:
    return update.message.reply_markdown(
      f'✋ No expense found with ID {expense_id}',
      quote=True,
    )

  reply = f'👌 Removed expense for @{expense.user} {format_currency(expense.amount)}'

  if expense.label.strip():
    reply += f': {expense.label}'

  try:
    db.session.delete(expense)
    db.session.commit()
  except Exception as exc:
    db.session.rollback()
    raise exc

  update.message.reply_markdown(
    reply,
    quote=False,
  )

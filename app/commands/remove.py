from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import format_currency, log, parse_int


def remove(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id

  try:
    expense_id = parse_int(context.args[0])
  except Exception as exc:
    log.exception('Parsing ID... %s: %s', 'ERR', exc)

    return update.message.reply_text(
      '💩 Looks like you didn\'t provide a valid expense ID (example: `/remove <expense_id>`)',
      parse_mode=ParseMode.MARKDOWN,
      quote=False,
    )

  expense = Expense.query.filter_by(id=expense_id, chat_id=chat_id).first()

  if expense is None:
    return update.message.reply_text(
      f'✋ No expense found with ID {expense_id}',
      parse_mode=ParseMode.MARKDOWN,
      quote=True,
    )

  reply = f'👌 Removed expense for @{expense.user} {format_currency(expense.amount)}'

  if expense.label.strip():
    reply += f': {expense.label}'

  db.session.delete(expense)
  db.session.commit()

  update.message.reply_text(
    reply,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

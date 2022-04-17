from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from ..utils import format_currency, log, parse_float


def add(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  user = update.message.from_user.username

  try:
    amount = parse_float(context.args[0])
  except Exception as exc:
    log.exception('Parsing amount... %s: %s', 'ERR', exc)

    return update.message.reply_text(
      '💩 Looks like you didn\'t provide a valid amount (example: `/add 99.99 <optional_label>`)',
      parse_mode=ParseMode.MARKDOWN,
      quote=False,
    )

  label = ' '.join(context.args[1:])

  expense = Expense(chat_id=chat_id, user=user, amount=amount, label=label)

  db.session.add(expense)
  db.session.commit()

  reply = f'👌 Added `{format_currency(amount)}` for @{user}'

  if label.strip():
    reply += f': {label}'

  update.message.reply_text(
    reply,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

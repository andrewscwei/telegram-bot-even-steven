from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..db import db


def error(update: Update, context: CallbackContext):
  db.session.rollback()

  update.message.reply_text(
    '💩 Something went wrong, please try again later',
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

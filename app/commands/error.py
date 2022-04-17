from telegram import Update
from telegram.ext import CallbackContext

from ..db import db
from ..utils import log


def error(update: Update, context: CallbackContext):
  chat_id = update.message.chat.id
  text = update.message.text
  exc = context.error

  log.exception('Handling message "%s" for chat ID <%s>... ERR: %s', text, chat_id, exc)

  db.session.rollback()

  update.message.reply_markdown_v2(
    '💩 Something went wrong, please try again later',
    quote=False,
  )

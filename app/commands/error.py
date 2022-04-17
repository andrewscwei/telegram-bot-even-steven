from telegram import Update
from telegram.ext import CallbackContext

from ..utils import log


def error(update: Update, context: CallbackContext):
  chat_id = update.message.chat.id
  text = update.message.text
  exc = context.error
  reply = str(exc) if str(exc).strip() else '💩 Something went wrong, please try again later'

  log.exception('Handling message "%s" for chat ID <%s>... %s', text, chat_id, 'ERR')

  update.message.reply_markdown(
    reply,
    quote=False,
  )

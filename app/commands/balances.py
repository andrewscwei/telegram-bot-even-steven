from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def balances(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  reply = 'Sorry! I\'m still working on this feature'

  update.message.reply_text(
    reply,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

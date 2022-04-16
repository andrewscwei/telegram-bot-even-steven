from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def polo(update: Update, context: CallbackContext):
  update.message.reply_text(
    'POLO',
    parse_mode=ParseMode.MARKDOWN,
    quote=True,
  )

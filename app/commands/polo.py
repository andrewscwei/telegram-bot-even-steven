from telegram import Update
from telegram.ext import CallbackContext


def polo(update: Update, context: CallbackContext):
  update.message.reply_markdown(
    'POLO',
    quote=False,
  )

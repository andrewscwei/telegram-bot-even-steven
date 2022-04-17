from telegram import Update
from telegram.ext import CallbackContext

from config import BUILD_NUMBER, VERSION


def version(update: Update, context: CallbackContext):
  update.message.reply_markdown(
    f'🤖 I\'m running on {VERSION}-{BUILD_NUMBER}',
    quote=False,
  )

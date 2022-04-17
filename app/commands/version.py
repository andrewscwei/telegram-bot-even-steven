from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from config import BUILD_NUMBER, VERSION


def version(update: Update, context: CallbackContext):
  update.message.reply_text(
    f'🤖 I\'m running on {VERSION}-{BUILD_NUMBER}',
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

from telegram import Update
from telegram.ext import CallbackContext

from .help_command import format_help_command


def unknown(update: Update, context: CallbackContext):
  reply = '🤔 I don\'t recognize that command'
  reply += '\n\n'
  reply += format_help_command()

  update.message.reply_markdown(
    reply,
    quote=False,
  )

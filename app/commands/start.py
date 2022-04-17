from telegram import Update
from telegram.ext import CallbackContext

from .help_command import format_help_command


def start(update: Update, context: CallbackContext):
  reply = 'Hi y\'all 🤘 my name is Even Steven. I\'m here to help split expenses _evenly_ for everyone!'
  reply += '\n\n'
  reply += format_help_command()

  update.message.reply_markdown(
    reply,
    quote=False,
  )

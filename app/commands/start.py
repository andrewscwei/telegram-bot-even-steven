from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
  text = 'Hi there 🤘 my name is Even Steven. I\'m here to help split expenses _evenly_ for you and your friends!'
  text += '\n\n'
  text += 'You can control me by sending these commands:'
  text += '\n\n'
  text += '/add - Adds an expense for a user, i.e. `/add 99.99 <optional_label>`'
  text += '\n'
  text += '/show - Shows the current balance for all users with tracked expenses'
  text += '\n'
  text += '/reset - Resets all tracked expenses'
  text += '\n'
  text += '/marco - 🧐'
  text += '\n'
  text += '/help - Shows available commands'

  update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

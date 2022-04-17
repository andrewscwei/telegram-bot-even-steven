from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
  text = 'Hi there 🤘 my name is Even Steven. I\'m here to help split expenses _evenly_ for you and your friends!'
  text += '\n\n'
  text += 'You can control me by sending these commands:'
  text += '\n\n'
  text += '/add - Adds an expense for the current user, i.e. `/add 99.99 <optional_label>`'
  text += '\n'
  text += '/remove - Removes an expense by its ID, i.e. `/remove <id>`'
  text += '\n'
  text += '/show - Shows all tracked expenses'
  text += '\n'
  text += '/balances - Checks current balances for all tracked users'
  text += '\n'
  text += '/clear - Clears all tracked expenses'
  text += '\n'
  text += '/marco - 🧐'
  text += '\n'
  text += '/help - Displays available commands'

  update.message.reply_text(
    text,
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

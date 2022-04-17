from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def help_command(update: Update, context: CallbackContext):
  update.message.reply_text(
    format_help_command(),
    parse_mode=ParseMode.MARKDOWN,
    quote=False,
  )

def format_help_command() -> str:
  ret = 'You can control me by sending these commands:'
  ret += '\n\n'
  ret += '/add - Adds an expense for the current user (example: `/add 99.99 <optional_label>`)'
  ret += '\n'
  ret += '/remove - Removes an expense by its ID (example: `/remove <id>`)'
  ret += '\n'
  ret += '/show - Shows all tracked expenses'
  ret += '\n'
  ret += '/balances - Checks current balances for all tracked users'
  ret += '\n'
  ret += '/clear - Clears all tracked expenses'

  return ret

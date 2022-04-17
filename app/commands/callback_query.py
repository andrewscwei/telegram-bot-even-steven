from telegram import Update
from telegram.ext import CallbackContext

from .clear import clear


def callback_query(update: Update, context: CallbackContext):
  query = update.callback_query
  query.answer()

  match query.data:
    case 'clear_yes':
      clear(query, context)
    case 'clear_no':
      query.edit_message_text(text='👌 Cancelled clear command')
    case _:
      query.delete_message()
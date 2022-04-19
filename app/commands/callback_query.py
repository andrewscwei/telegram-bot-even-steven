from telegram import Update
from telegram.ext import CallbackContext

from .clear import clear_query_no, clear_query_yes


def callback_query(update: Update, context: CallbackContext):
  query = update.callback_query
  query.answer()

  match query.data:
    case 'clear_yes':
      clear_query_yes(query, context)
    case 'clear_no':
      clear_query_no(query, context)
    case _:
      query.delete_message()

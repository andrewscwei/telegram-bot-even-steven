from telegram import (CallbackQuery, InlineKeyboardButton,
                      InlineKeyboardMarkup, ParseMode, Update)
from telegram.ext import CallbackContext

from ..db import db
from ..models import Expense
from .balances import format_balances


def clear(update: Update, context: CallbackContext):
  keyboard = [
    [InlineKeyboardButton('Yes', callback_data='clear_yes')],
    [InlineKeyboardButton('Cancel', callback_data='clear_no')],
  ]

  update.message.reply_text(
    '✋ Are you sure you want to clear all expenses?',
    reply_markup=InlineKeyboardMarkup(keyboard),
    quote=False,
  )

def clear_query(query: CallbackQuery, context: CallbackContext):
  chat_id = query.message.chat.id
  expenses = Expense.query.filter_by(chat_id=chat_id)

  if expenses.count() < 1:
    query.edit_message_text(
      'Nothing to clear 🙃',
      parse_mode=ParseMode.MARKDOWN,
    )
  else:
    try:
      expenses_by_user = db.session.query(Expense.user, db.func.sum(Expense.amount)).filter_by(chat_id=chat_id).group_by(Expense.user).all()
      balances_str = format_balances(expenses_by_user)
      expenses.delete()
      db.session.commit()
    except Exception as exc:
      db.session.rollback()
      raise exc

    reply = '👌 All expenses are cleared, below are the last known balances:'
    reply += '\n\n'
    reply += balances_str

    query.edit_message_text(
      reply,
      parse_mode=ParseMode.MARKDOWN,
    )

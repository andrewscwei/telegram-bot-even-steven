from telegram import Update
from telegram.ext import CallbackContext


def show(update: Update, context: CallbackContext):
  update.message.reply_text('Sorry, this function is still under development!')

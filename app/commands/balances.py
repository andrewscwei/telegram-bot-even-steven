from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..utils import log


def balances(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id

  try:
    reply = 'Sorry! I\'m still working on this feature'

    update.message.reply_text(
      reply,
      parse_mode=ParseMode.MARKDOWN,
      quote=False,
    )

  except Exception as exc:
    log.exception('Showing balances for chat ID %s... %s: %s', chat_id, 'ERR', exc)

    update.message.reply_text(
      '💩 Something went wrong, please try again later',
      parse_mode=ParseMode.MARKDOWN,
      quote=False,
    )

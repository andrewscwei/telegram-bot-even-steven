from telegram import Bot
from telegram.ext import CommandHandler, Dispatcher

from config import BOT_TOKEN

from .commands import add, balances, clear, error, polo, show, start
from .utils import log


def create_dispatcher():
  try:
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot, None, workers=1)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', start))
    dispatcher.add_handler(CommandHandler('add', add))
    dispatcher.add_handler(CommandHandler('show', show))
    dispatcher.add_handler(CommandHandler('balance', balances))
    dispatcher.add_handler(CommandHandler('balances', balances))
    dispatcher.add_handler(CommandHandler('reset', clear))
    dispatcher.add_handler(CommandHandler('clear', clear))
    dispatcher.add_handler(CommandHandler('marco', polo))
    dispatcher.add_error_handler(error)

    log.info('Initializing bot... %s', 'OK')

    return dispatcher
  except Exception as exc:
    log.exception('Initializing bot... %s: %s', 'ERR', exc)

    return None

dispatcher = create_dispatcher()

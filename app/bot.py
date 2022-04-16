from telegram import Bot
from telegram.ext import CommandHandler, Dispatcher

from config import BOT_TOKEN

from .commands import add, polo, reset, show, start
from .utils import log


def create_dispatcher():
  try:
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot, None, workers=1)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', start))
    dispatcher.add_handler(CommandHandler('add', add))
    dispatcher.add_handler(CommandHandler('show', show))
    dispatcher.add_handler(CommandHandler('reset', reset))
    dispatcher.add_handler(CommandHandler('marco', polo))

    log.info('Initializing bot... %s', 'OK')

    return dispatcher
  except Exception as exc:
    log.exception('Initializing bot... %s: %s', 'ERR', exc)

    return None

dispatcher = create_dispatcher()

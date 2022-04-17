from telegram import Bot
from telegram.ext import (CallbackQueryHandler, CommandHandler, Dispatcher,
                          Filters, MessageHandler)

from config import BOT_TOKEN

from .commands import (add, balances, callback_query, clear, error,
                       help_command, polo, remove, show, start, unknown,
                       version)
from .utils import log


def create_dispatcher():
  try:
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot, None, workers=1)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler(['h', 'help'], help_command))
    dispatcher.add_handler(CommandHandler(['a', 'add'], add))
    dispatcher.add_handler(CommandHandler(['s', 'show', 'l', 'ls', 'list', 'all', 'expense', 'expenses', 'entry', 'entries', 'record', 'records'], show))
    dispatcher.add_handler(CommandHandler(['r', 'rm', 'remove', 'd', 'del', 'delete', 'erase'], remove))
    dispatcher.add_handler(CommandHandler(['b', 'balance', 'balances'], balances))
    dispatcher.add_handler(CommandHandler(['c', 'clr', 'clear', 'reset'], clear))
    dispatcher.add_handler(CommandHandler(['v', 'ver', 'version'], version))
    dispatcher.add_handler(CommandHandler(['marco'], polo))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    dispatcher.add_handler(CallbackQueryHandler(callback_query))
    dispatcher.add_error_handler(error)

    log.info('Initializing bot... %s', 'OK')

    return dispatcher
  except Exception as exc:
    log.exception('Initializing bot... %s: %s', 'ERR', exc)

    return None

dispatcher = create_dispatcher()

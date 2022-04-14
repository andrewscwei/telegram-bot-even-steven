from telegram import Bot
from telegram.ext import CommandHandler, Dispatcher

from app.commands.add import add
from app.commands.polo import polo
from app.commands.reset import reset
from app.commands.show import show
from app.commands.start import start
from app.utils.log import log


def setup_bot(token: str):
  try:
    bot = Bot(token)
    dispatcher = Dispatcher(bot, None, workers=0)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("add", add))
    dispatcher.add_handler(CommandHandler("show", show))
    dispatcher.add_handler(CommandHandler("reset", reset))
    dispatcher.add_handler(CommandHandler("marco", polo))

    log.info("Starting bot... %s", "OK")

    return dispatcher
  except Exception as exc:
    log.exception("Starting bot... %s: %s", "ERR", exc)

    return None

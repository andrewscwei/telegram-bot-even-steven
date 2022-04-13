from telegram import Bot


def marco_polo(bot: Bot, chat_id: str) -> None:
  bot.send_message(chat_id, "Polo")

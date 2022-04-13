from telegram import Bot
from app.utils import send_message

def marco_polo(bot: Bot, chat_id: str):
  send_message(bot, chat_id, "Polo")

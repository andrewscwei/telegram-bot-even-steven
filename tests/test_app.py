import os

from app import dispatcher


def test_bot_token():
  assert 'BOT_TOKEN' in os.environ

def test_bot_dispatcher():
  assert dispatcher is not None
  assert dispatcher.bot is not None
  assert dispatcher.bot.token is not None

import os

from dotenv import load_dotenv

load_dotenv

def test_ensure_token():
  assert "TELEGRAM_BOT_TOKEN" in os.environ

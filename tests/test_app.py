import os

from dotenv import load_dotenv

load_dotenv

def test_token():
  assert "BOT_TOKEN" in os.environ

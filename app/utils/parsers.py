from telegram import User


def parse_float(value) -> float:
  ret = float(value)
  return ret

def parse_int(value) -> int:
  ret = int(value)
  return ret

def parse_user(user: User) -> str:
  username = user.username
  first_name = user.first_name
  return f'@{username}' if username.strip() else first_name

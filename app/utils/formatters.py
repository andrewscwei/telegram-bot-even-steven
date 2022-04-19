from .parsers import parse_float


def format_currency(value) -> str:
  amount = parse_float(value)
  rounded = '{:.2f}'.format(abs(amount))

  if amount >= 0:
    return f'${rounded}'
  else:
    return f'-${rounded}'

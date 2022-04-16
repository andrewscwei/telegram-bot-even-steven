from .parsers import parse_float


def format_currency(value) -> str:
  amount = parse_float(value)
  rounded = '{:.2f}'.format(amount)
  ret = f'${rounded}'
  return ret

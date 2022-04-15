import logging
import os

COLOR_PREFIX = "\033["
COLOR_RESET = f"{COLOR_PREFIX}0m"
COLOR_BLACK = f"{COLOR_PREFIX}0;30m"
COLOR_RED = f"{COLOR_PREFIX}0;31m"
COLOR_GREEN = f"{COLOR_PREFIX}0;32m"
COLOR_YELLOW = f"{COLOR_PREFIX}0;33m"
COLOR_BLUE = f"{COLOR_PREFIX}0;34m"
COLOR_PURPLE = f"{COLOR_PREFIX}0;35m"
COLOR_CYAN = f"{COLOR_PREFIX}0;36m"
COLOR_LIGHT_GRAY = f"{COLOR_PREFIX}0;37m"

if os.environ.get("FLASK_ENV") == "development":
  logging.basicConfig(
    level=logging.DEBUG,
    format=f"{COLOR_CYAN}%(name)s:{COLOR_RESET} {COLOR_GREEN}%(levelname)s{COLOR_RESET} %(message)s",
  )
else:
  logging.basicConfig(
    level=logging.DEBUG,
    format=f"{COLOR_CYAN}%(name)s:{COLOR_RESET} {COLOR_GREEN}%(levelname)s{COLOR_RESET} %(message)s",
  )

log = logging.getLogger("bot")

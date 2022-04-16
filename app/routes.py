import http

import requests
import telegram
from flask import Blueprint, Response, request

from config import BUILD_NUMBER, REBASE_URL

from .bot import dispatcher
from .db import test_db

routes = Blueprint('routes', __name__, url_prefix='/')

@routes.get('/health')
def health_check() -> Response:
  return {
    'bot': 'up' if dispatcher is not None else 'down',
    'build': BUILD_NUMBER,
    'db': 'up' if test_db() else 'down',
  }, http.HTTPStatus.OK

@routes.get('/info')
def info() -> Response:
  return requests.get(f'https://api.telegram.org/bot{dispatcher.bot.token}/getMe').content

@routes.get('/rebase')
def reset() -> Response:
  if REBASE_URL is None:
    return { 'error': 'No rebase URL provided' }, http.HTTPStatus.INTERNAL_SERVER_ERROR

  return requests.get(
    f'https://api.telegram.org/bot{dispatcher.bot.token}/setWebhook?url={REBASE_URL}'
  ).content

@routes.post('/')
def index() -> Response:
  if dispatcher is None:
    return 'Bot is inactive', http.HTTPStatus.INTERNAL_SERVER_ERROR

  update = telegram.Update.de_json(request.get_json(force=True), dispatcher.bot)
  dispatcher.process_update(update)

  return '', http.HTTPStatus.NO_CONTENT

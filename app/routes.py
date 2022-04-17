import http

import requests
import telegram
from flask import Blueprint, Response, request
from sqlalchemy_utils import create_database, database_exists

from config import BUILD_NUMBER, DATABASE_URL, REBASE_URL, VERSION

from .bot import dispatcher
from .db import db, test_db
from .utils import log

routes = Blueprint('routes', __name__, url_prefix='/')

@routes.get('/health')
def health_check() -> Response:
  try:
    if not database_exists(DATABASE_URL):
      create_database(DATABASE_URL)
    db.create_all()
  except Exception as exc:
    log.exception('Health checking database... %s: %s', 'ERR', exc)

  return {
    'bot': 'up' if dispatcher is not None else 'down',
    'version': f'{VERSION}-{BUILD_NUMBER}',
    'db': 'up' if test_db() else 'down',
  }, http.HTTPStatus.OK

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

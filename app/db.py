from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from config import DATABASE_URL

from .utils.log import log

db = SQLAlchemy()

def init_db(app: Flask):
  app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)

  log.info('Initializing database... %s: %s', 'OK', db)

def test_db() -> bool:
  try:
    db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    log.info('Testing database connection... %s', 'OK')

    return True
  except Exception as exc:
    log.exception('Testing database connection... %s: %s', 'ERR', exc)

    return False

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy_utils import create_database, database_exists

from config import DATABASE_URL

from .utils.log import log

db = SQLAlchemy()

def init_db(app: Flask):
  try:
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    if not database_exists(DATABASE_URL):
      log.info('Verifying that database exists... %s: %s', 'OK', 'Database(s) missing, creating missing database(s)')
      create_database(DATABASE_URL)
    else:
      log.info('Verifying that database exists... %s: %s', 'OK', 'Database(s) are in place')

    log.info('Initializing database... %s: %s', 'OK', db)
  except Exception as exc:
    log.exception('Initializing database... %s: %s', 'ERR', exc)

  with app.app_context():
    db.create_all()

def test_db() -> bool:
  try:
    db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    log.info('Testing database connection... %s', 'OK')

    return True
  except Exception as exc:
    log.exception('Testing database connection... %s: %s', 'ERR', exc)

    return False

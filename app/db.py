import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy_utils import create_database, database_exists

from .utils.log import log


def setup_db(app: Flask) -> SQLAlchemy:
  try:
    log.info("Initializing database...")

    url = os.environ.get('DATABASE_URL')

    if url.startswith("postgres://"):
      url = url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)

    if not database_exists(url):
      log.info("Verifying that database exists... %s: %s", "OK", "Database(s) missing, creating missing database(s)")
      create_database(url)
    else:
      log.info("Verifying that database exists... %s: %s", "OK", "Database(s) are in place")

    log.info("Initializing database... %s: %s", "OK", db)

    return db
  except Exception as exc:
    log.exception("Initializing database... %s: %s", "ERR", exc)

    return None

def test_db(db: SQLAlchemy) -> bool:
  try:
    db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    log.info("Testing database connection... %s", "OK")
    return True
  except Exception as exc:
    log.exception("Testing database connection... %s: %s", "ERR", exc)
    return False

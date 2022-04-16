from .db import db


class Transaction(db.Model):
  __tablename__ = 'transactions'

  id = db.Column(db.Integer, primary_key=True)
  chat_id = db.Column(db.String())

  def __init__(self, chat_id):
    self.chat_id = chat_id

from .db import db


class Expense(db.Model):
  __tablename__ = 'expenses'

  id = db.Column(db.Integer, primary_key=True)
  chat_id = db.Column(db.String())
  user = db.Column(db.String())
  amount = db.Column(db.Float())
  label = db.Column(db.Text())
  created_at = db.Column(db.DateTime(), server_default=db.func.now())
  updated_at = db.Column(db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now())

  def __init__(self, chat_id, user, amount, label=None):
    self.chat_id = chat_id
    self.user = user
    self.amount = amount
    self.label = label

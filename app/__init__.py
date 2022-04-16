from flask import Flask

from .db import init_db
from .routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

init_db(app)

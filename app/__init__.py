from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.API import bp as api_bp

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app import models, routes
app.register_blueprint(api_bp, url_prefix='/api')

with app.app_context():
    db.create_all()
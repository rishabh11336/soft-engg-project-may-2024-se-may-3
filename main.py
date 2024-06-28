from flask import Flask
from application.config import DevelopmentConfig
from application.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app=app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()
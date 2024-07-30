from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.thing import bp as thing_bp

    app.register_blueprint(thing_bp, url_prefix="/v1")

    return app


from app import models  # noqa: F401, E402

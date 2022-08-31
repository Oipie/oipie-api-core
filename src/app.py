"""
Main entrypoint
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config.db import DATABASE_URL_CONECTION
# pylint: disable=import-outside-toplevel

db = SQLAlchemy()


def create_app():
    """
    create and configure the app
    """
    app = Flask(__name__, instance_relative_config=True)

    print(DATABASE_URL_CONECTION)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=DATABASE_URL_CONECTION
    )

    db.init_app(app)

    from .api.health.health_controller import health_bp
    app.register_blueprint(health_bp)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app

    # pylint: enable=import-outside-toplevel

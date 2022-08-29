"""
Main entrypoint
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config.db import DATABASE_CONFIG

db = SQLAlchemy()


def create_app():
    """
    create and configure the app
    """
    app = Flask(__name__, instance_relative_config=True)
    print(DATABASE_CONFIG)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=(
            "postgresql://{host}:{port}/{database_name}?user={username}&password={password}"
            .format(**DATABASE_CONFIG)
        )
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

"""
Main entrypoint
"""
import os
from flask import Flask
from flask_migrate import Migrate
from src.config.db import DATABASE_URL_CONECTION

# pylint: disable=import-outside-toplevel


def create_app():
    """
    create and configure the app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=DATABASE_URL_CONECTION,
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
    )

    from src.config.container import Container

    app.container = Container()

    migrate = Migrate(directory="./src/config/migrations")
    migrate.init_app(app, app.container.db)

    from .api.health.health_controller import health_bp

    app.register_blueprint(health_bp)
    from .api.recipes.recipes_controller import recipes_bp

    app.register_blueprint(recipes_bp)

    from .api.shared.handle_http_exception import errors_bp

    app.register_blueprint(errors_bp)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app

    # pylint: enable=import-outside-toplevel

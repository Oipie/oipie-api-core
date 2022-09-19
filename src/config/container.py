"""
    Configuration of dependency injection module
"""
from dependency_injector import containers, providers
from sqlalchemy import create_engine as create_engine_sqlalchemy
from src.config.database import Database
from src.config.db import database_url_connection
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.core.users.infrastructure.user_repository_sqlalchemy import UsersRepositorySQLAlchemy
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.application.users_login import UsersLogin
from src.shared.services.password.argon2_password import Argon2Password


def create_engine(url_connection: str):
    """
    Creates an engine
    """
    engine = create_engine_sqlalchemy(url_connection)
    connection = engine.connect()
    yield connection
    connection.close()


class Container(containers.DeclarativeContainer):
    """
    Dependency injection container
    """

    wiring_config = containers.WiringConfiguration(packages=["..api"])

    connection = providers.Resource(create_engine, url_connection=database_url_connection())
    password_hasher = providers.Singleton(Argon2Password)
    db = providers.Factory(Database, connection=connection)

    # pylint: disable=no-member
    recipes_repository = providers.Singleton(
        RecipesRepositorySQLAlchemy, session_factory=db.provided.session
    )
    users_repository = providers.Singleton(
        UsersRepositorySQLAlchemy, session_factory=db.provided.session
    )
    users_registerer = providers.Singleton(
        UsersRegisterer, users_repository=users_repository, password_hasher=password_hasher
    )
    users_login = providers.Singleton(
        UsersLogin, users_repository=users_repository, password_hasher=password_hasher
    )

    # pylint: enable=no-member

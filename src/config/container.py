"""
    Configuration of dependency injection module
"""
from dependency_injector import containers, providers
from sqlalchemy import create_engine as create_engine_sqlalchemy
from src.config.database_handler import DatabaseHandler
from src.config.db import database_url_connection
from src.config.jwt import JWT_SECRET_KEY
from src.config.session_handler import SessionHandler
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.core.users.infrastructure.user_repository_sqlalchemy import UsersRepositorySQLAlchemy
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.application.users_login import UsersLogin
from src.shared.services.password.argon2_password import Argon2Password
from src.shared.services.tokenizer.jwt_tokenizer import JwtTokenizer


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
    database_handler = providers.Singleton(DatabaseHandler, connection=connection)
    session_handler = providers.Factory(
        SessionHandler,
        connection=connection,
    )

    tokenizer = JwtTokenizer(JWT_SECRET_KEY)

    recipes_repository = providers.Singleton(
        RecipesRepositorySQLAlchemy, session_handler=session_handler
    )
    users_repository = providers.Singleton(
        UsersRepositorySQLAlchemy, session_handler=session_handler
    )
    users_registerer = providers.Singleton(
        UsersRegisterer, users_repository=users_repository, password_hasher=password_hasher
    )
    users_login = providers.Singleton(
        UsersLogin,
        users_repository=users_repository,
        password_hasher=password_hasher,
        tokenizer=tokenizer,
    )

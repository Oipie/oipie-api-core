"""
This module serves the purpose of perform several actions on the recipes
"""

from dependency_injector.wiring import Provide, inject
from flask import Blueprint
from src.config.container import Container
from src.core.recipes.application.recipes_lister import RecipesLister
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy \
    import RecipesRepositorySQLAlchemy


recipes_bp = Blueprint('recipes_bp', __name__)


@recipes_bp.route("/recipes", methods=['GET'])
@inject
def index(
    recipes_repository: RecipesRepositorySQLAlchemy = Provide[Container.recipes_repository]
):
    """
    This route returns a 200 OK returning all recipes existing in database
    """

    lister = RecipesLister(recipes_repository)
    return list(map(lambda recipie: recipie.serialize(), lister.execute()))

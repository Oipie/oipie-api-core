"""
This module serves the purpose of perform several actions on the recipes
"""

from flask import Blueprint
from src.core.recipes.application.recipies_lister import RecipiesLister
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy \
    import RecipesRepositorySQLAlchemy
from src.app import db

recipes_bp = Blueprint('recipes_bp', __name__)
recipies_lister = RecipiesLister(RecipesRepositorySQLAlchemy(db.session))


@recipes_bp.route("/recipes", methods=['GET'])
def index():
    """
    This route returns a 200 OK returning all recipes existing in database
    """

    return list(map(lambda recipie: recipie.serialize(), recipies_lister.execute()))
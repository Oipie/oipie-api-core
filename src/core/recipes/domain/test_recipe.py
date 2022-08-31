"""
Tests to check Recipe class
"""
import uuid
from tests.fixtures.recipe_fixture import PANCAKE
from .recipe import Recipe, RecipeAttributes


def test_serialize_is_ok():
    """
    Checks serialize serializes a recipe as expected
    """
    recipe_attributes: RecipeAttributes = PANCAKE
    recipe = Recipe(recipe_attributes)

    result = recipe.serialize()

    assert result == recipe_attributes


def test_serialize_is_not_equal():
    """
    Checks serialize serializes a recipe differently of another
    """
    recipe_attributes: RecipeAttributes = PANCAKE
    recipe_attributes_changed: RecipeAttributes = {
        "id_": 2,
        "uuid": str(uuid.uuid4()),
        "name": 'Strawberry smoothie',
        "favourite": False,
        "favourite_amount": 20,
        "preparation_time": 8500,
        "cover": 'http://an-url.com/a/smoothie.png',
    }
    recipe = Recipe(recipe_attributes_changed)

    result = recipe.serialize()

    assert result != recipe_attributes

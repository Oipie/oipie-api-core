"""
Tests to check Recipe class
"""

from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE
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
    recipe_attributes_changed: RecipeAttributes = STRAWBERRY_SMOOTHIE
    recipe = Recipe(recipe_attributes_changed)

    result = recipe.serialize()

    assert result != recipe_attributes

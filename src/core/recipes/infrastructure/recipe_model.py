"""
Recipe Database Model
"""
import uuid
from sqlalchemy.dialects.postgresql import UUID
from src.app import db
from src.core.recipes.domain.recipe import Recipe


class RecipeModel(db.Model):
    """
    This class represents a Recipe in database model
    """
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    name = db.Column(db.String, nullable=False)
    favourite_amount = db.Column(db.Integer, default=0, nullable=False)
    preparation_time = db.Column(db.Integer, default=0, nullable=False)
    cover = db.Column(db.String)

    @staticmethod
    def from_domain_object(recipe: Recipe):
        """
        Transforms to Recipe model
        """
        return RecipeModel(id=recipe.id_, uuid=recipe.uuid, name=recipe.uuid,
                           favourite_amount=recipe.favourite_amount,
                           preparation_time=recipe.preparation_time, cover=recipe.preparation_time)

    def to_domain_object(self) -> Recipe:
        """
        Transforms Recipe database model to a domain object
        """
        return Recipe({
            'id_': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'favourite_amount': self.favourite_amount,
            'preparation_time': self.preparation_time,
            'cover': self.cover,
        })

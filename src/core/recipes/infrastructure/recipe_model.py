"""
Recipe Database Model
"""
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer
from src.config.database_handler import Models
from src.core.recipes.domain.recipe import Recipe


class RecipeModel(Models):
    """
    This class represents a Recipe in database model
    """

    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    favourite_amount = Column(Integer, default=0, nullable=False)
    preparation_time = Column(Integer, default=0, nullable=False)
    cover = Column(String)

    @staticmethod
    def from_domain_object(recipe: Recipe):
        """
        Transforms to Recipe model
        """
        return RecipeModel(
            id=recipe.id_,
            uuid=recipe.uuid,
            name=recipe.uuid,
            favourite_amount=recipe.favourite_amount,
            preparation_time=recipe.preparation_time,
            cover=recipe.preparation_time,
        )

    def to_domain_object(self) -> Recipe:
        """
        Transforms Recipe database model to a domain object
        """
        return Recipe(
            {
                "id_": self.id,
                "uuid": self.uuid,
                "name": self.name,
                "favourite_amount": self.favourite_amount,
                "preparation_time": self.preparation_time,
                "cover": self.cover,
            }
            # {
            #     "id_": cast(self.id, Integer),
            #     "uuid": cast(self.uuid, String),
            #     "name": cast(self.name, String),
            #     "favourite_amount": cast(self.favourite_amount, Integer),
            #     "preparation_time": cast(self.preparation_time, Integer),
            #     "cover": cast(self.cover, String),
            # }
        )

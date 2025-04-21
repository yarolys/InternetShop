from src.data_layer.alchemy.models.review import Review
from src.resources.base import BaseEntity


class ReviewEntity(BaseEntity):
    db_object = Review
from src.data_layer.alchemy.models.order import Order
from src.resources.base import BaseEntity


class Entity(BaseEntity):
    db_object = Order
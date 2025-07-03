from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    """
    Схема для создания продукта.

    Attributes:
        name (str): Название продукта.
        category_id (int): Идентификатор категории, к которой принадлежит продукт.
        quantity (int): Количество продукта на складе.
    """
    name: str
    category_id: int
    quantity: int


class ProductSchema(ProductCreateSchema):
    """
    Схема для представления продукта.

    Наследует атрибуты из ProductCreateSchema и добавляет уникальный идентификатор.

    Attributes:
        id (int): Уникальный идентификатор продукта.
    """
    id: int

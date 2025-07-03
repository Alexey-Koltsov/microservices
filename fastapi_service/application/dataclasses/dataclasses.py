from attr import dataclass


@dataclass
class Category:
    """Модель категории товара"""
    id: int | None
    name: str


@dataclass
class Product:
    """Модель товара"""
    name: str
    quantity: int
    id: int | None = None
    category_id: int | None = None

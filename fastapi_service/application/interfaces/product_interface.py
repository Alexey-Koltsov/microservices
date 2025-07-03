from abc import ABC, abstractmethod

from application.dataclasses.dataclasses import Product
from routing.schemas.product_schemas import ProductCreateSchema


class ProductInterface(ABC):
    """Интерфейс для продукта"""

    @abstractmethod
    async def get_products(self) -> list[Product]:
        """Метод для получения продуктов"""
        pass

    async def get_product(self, product_id: int) -> Product | None:
        """Метод для получения продукта по id"""
        pass

    @abstractmethod
    async def create_product(
        self,
        create_data: ProductCreateSchema,
    ) -> Product:
        """Метод для создания продукта"""
        pass

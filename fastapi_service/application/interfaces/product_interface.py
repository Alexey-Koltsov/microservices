from abc import ABC, abstractmethod
from typing import List

from adapters.database.tables.models_db import Product
from application.dataclass.product import ProductDTO
from routing.schemas.product_schemas import ProductCreateSchema


class ProductInterface(ABC):
    """Интерфейс для продукта"""

    @abstractmethod
    async def get_products(self) -> List[ProductDTO]:
        """Метод для получения продуктов"""
        pass

    async def get_product(self, product_id: int) -> ProductDTO | None:
        """Метод для получения продукта по id"""
        pass

    @abstractmethod
    async def create_product(
        self,
        create_data: ProductCreateSchema,
    ) -> ProductDTO:
        """Метод для создания продукта"""
        pass

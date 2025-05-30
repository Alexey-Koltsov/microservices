from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.tables import Product
from schemas.product_schemas import ProductCreateSchema


class ProductInterface(ABC):
    """Интерфейс для продукта"""

    @staticmethod
    @abstractmethod
    async def get_products(
        self,
        db: AsyncSession
    ) -> List[Product]:
        """Метод для получения продуктов"""
        pass

    @staticmethod
    @abstractmethod
    async def create_product(
        self,
        create_data: ProductCreateSchema,
        db: AsyncSession
    ) -> Product:
        """Метод для создания продукта"""
        pass

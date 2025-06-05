from abc import ABC, abstractmethod
from typing import List

from application.dataclass.product import ProductDTO
from routing.schemas.product_schemas import ProductCreateSchema


class ProductInterface(ABC):
    """Интерфейс для продукта"""

    @abstractmethod
    async def get_products(self) -> List[ProductDTO]:
        """Метод для получения продуктов"""
        pass

    @abstractmethod
    async def create_product(
        self,
        create_data: ProductCreateSchema,
    ) -> ProductDTO:
        """Метод для создания продукта"""
        pass

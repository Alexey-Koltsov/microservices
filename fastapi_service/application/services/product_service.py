from typing import List

from application.dataclass.product import ProductDTO
from application.interfaces.product_interface import ProductInterface
from attr import frozen

from routing.schemas.product_schemas import ProductCreateSchema


@frozen
class ProductService:
    product_repository: ProductInterface

    async def get_products(self) -> List[ProductDTO]:
        result = await self.product_repository.get_products()
        return result

    async def get_product(self, product_id: int) -> ProductDTO | None:
        result = await self.product_repository.get_product(
            product_id=product_id
        )
        return result

    async def create_product_service(
        self,
        create_data: ProductCreateSchema,
    ) -> ProductDTO:
        result = await self.product_repository.create_product(
            create_data=create_data
        )
        return result

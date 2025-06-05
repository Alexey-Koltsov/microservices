from typing import List

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.tables.models_db import Product
from application.dataclass.product import ProductDTO
from application.interfaces.product_interface import ProductInterface
from routing.schemas.product_schemas import ProductCreateSchema


class ProductRepository(ProductInterface):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_products(self) -> List[ProductDTO]:
        stmt = select(Product)
        results = await self.session.execute(stmt)
        products = [ProductDTO(id=result.id, name=result.name,
                               category_id=result.category_id,
                               quantity=result.quantity)
                    for result in results.scalars().all()]
        return products

    async def create_product(
            self,
            create_data: ProductCreateSchema,
    ) -> ProductDTO:
        create_data_dict = create_data.dict()
        stmt = insert(Product).values(**create_data_dict).returning(Product)
        results = await self.session.execute(stmt)
        result = results.scalars().one()
        product = ProductDTO(id=result.id,
                             name=result.name,
                             category_id=result.category_id,
                             quantity=result.quantity)

        return product

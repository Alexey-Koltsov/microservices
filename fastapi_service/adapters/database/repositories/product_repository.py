from typing import List

from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.tables import Product
from application.interfaces.product_interface import ProductInterface
from database.database import get_db_session
from schemas.product_schemas import ProductCreateSchema


class ProductRepository(ProductInterface):

    @staticmethod
    async def get_products(
        db: AsyncSession = Depends(get_db_session)
    ) -> List[Product]:
        stmt = select(Product)
        results = await db.execute(stmt)
        products = [Product(result) for result in results.all()]
        return products

    @staticmethod
    async def create_product(
            create_data: ProductCreateSchema,
            db: AsyncSession = Depends(get_db_session)
    ) -> Product:
        create_data_dict = create_data.dict()
        stmt = insert(Product).values(**create_data_dict).returning(Product)
        result = await db.execute(stmt)
        await db.commit()

        return result.scalars().first()

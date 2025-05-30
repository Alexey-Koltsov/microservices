from typing import List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.repositories.product_repository import ProductRepository
from adapters.database.tables import Product
from database.database import get_db_session
from schemas.product_schemas import ProductCreateSchema


class ProductService:

    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    @staticmethod
    async def get_products(
        self,
        db: AsyncSession = Depends(get_db_session)
    ) -> List[Product]:
        result = await self.repository.get_products(db=db)
        return result

    @staticmethod
    async def create_product(
        self,
        create_data: ProductCreateSchema,
        db: AsyncSession = Depends(get_db_session),
    ) -> Product:
        result = await self.repository.create_product(
            create_data=create_data,
            db=db
        )
        return result

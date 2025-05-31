from typing import List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.repositories.product_repository import ProductRepository
from adapters.database.tables import Product
from database.database import get_db_session
from depends.depends_repositories import get_product_repository
from schemas.product_schemas import ProductCreateSchema


class ProductService:

    @staticmethod
    async def get_products_service(
        db: AsyncSession = Depends(get_db_session),
        repository: ProductRepository = Depends(get_product_repository)
    ) -> List[Product]:
        result = await repository.get_products(db=db)
        return result

    @staticmethod
    async def create_product_service(
        create_data: ProductCreateSchema,
        db: AsyncSession = Depends(get_db_session),
        repository: ProductRepository = Depends(get_product_repository)
    ) -> Product:
        result = await repository.create_product(
            create_data=create_data,
            db=db
        )
        return result

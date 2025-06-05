from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.repositories.product_repository import ProductRepository
from application.services.product_service import ProductService
from adapters.database.database import get_async_session

"""
Файл внедрения зависимостей для слоя репозиториев
"""
# repository - работа с БД


def create_product_repository(
        session: AsyncSession = Depends(get_async_session),
) -> ProductRepository:
    return ProductRepository(session=session)


def create_product_service(
        product_repository: ProductRepository = Depends(
            create_product_repository),
) -> ProductService:
    return ProductService(product_repository=product_repository)

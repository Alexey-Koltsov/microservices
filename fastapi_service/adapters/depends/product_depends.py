from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.repositories.product_repository import ProductRepository
from application.services.product_service import ProductService
from adapters.database.settings import get_async_session


def create_product_repository(
        session: AsyncSession = Depends(get_async_session),
) -> ProductRepository:
    """Внедрения зависимостей для слоя репозиториев"""
    return ProductRepository(session=session)


def create_product_service(
        product_repository: ProductRepository = Depends(
            create_product_repository),
) -> ProductService:
    """Внедрения зависимостей для слоя сервисов"""
    return ProductService(product_repository=product_repository)

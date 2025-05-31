from application.services.product_service import ProductService
from .depends_repositories import product_repository

"""
Файл внедрения зависимостей для слоя сервисов
"""
# service - слой UseCase
product_service: ProductService = ProductService(product_repository)


def get_product_service() -> ProductService:
    return product_service

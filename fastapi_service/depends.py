from adapters.database.repositories.product_repository import ProductRepository
from application.services.product_service import ProductService


"""
Файл внедрения зависимостей
"""
# repository - работа с БД
product_repository = ProductRepository()

# service - слой UseCase
product_service = ProductService(product_repository)


def get_product_service() -> ProductService:
    return product_service

from adapters.database.repositories.product_repository import ProductRepository


"""
Файл внедрения зависимостей для слоя репозиториев
"""
# repository - работа с БД
product_repository: ProductRepository = ProductRepository()


def get_product_repository() -> ProductRepository:
    return product_repository

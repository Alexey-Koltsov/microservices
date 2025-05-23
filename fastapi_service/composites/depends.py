from adapters.items import ItemRepository
from application.items import ItemService

"""
Файл внедрения зависимостей
"""
# repository - работа с БД
item_repository = ItemRepository()

# service - слой UseCase
item_service = ItemService(item_repository)


def get_item_service() -> ItemService:
    return item_service

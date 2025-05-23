from typing import List

from adapters.items import ItemRepository
from schemas.items import Item


class ItemService:

    def __init__(self, repository: ItemRepository) -> None:
        self.repository = repository

    def get_items(self) -> List[Item]:
        result = self.repository.get_items()
        return result

    def create_item(self) -> Item:
        result = self.repository.create_item()
        return result

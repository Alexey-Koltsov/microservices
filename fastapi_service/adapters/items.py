from typing import List

from schemas.items import Item


class ItemRepository:

    def get_items(self) -> List[Item]:
        ...

    def create_item(self) -> Item:
        ...

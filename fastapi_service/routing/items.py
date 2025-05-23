from typing import List, Optional

from fastapi import APIRouter, Depends

from schemas.items import Item
from application.items import ItemService
from composites.depends import get_item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.get(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=List[Item],
    description="Получение листинга всех продуктов",
)
async def get_all_items(
    item_service: ItemService = Depends(get_item_service),
) -> Optional[List[Item]]:
    items = item_service.get_items()
    return items


@router.post(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=Item,
    description="Создание товара",
)
async def get_all_items(
       item_service: ItemService = Depends(get_item_service),
) -> Item:
    item = item_service.create_item()
    return item

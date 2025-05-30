from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from schemas.product_schemas import ProductSchema, ProductCreateSchema
from application.services import ProductService
from depends import get_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=List[ProductSchema],
    description="Получение листинга всех продуктов",
)
async def get_all_products(
    self,
    db: AsyncSession = Depends(get_db_session),
    product_service: ProductService = Depends(get_product_service),
) -> Optional[List[ProductSchema]]:
    products = await self.product_service.get_products(db=db)
    return products


@router.post(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=ProductSchema,
    description="Создание товара",
)
async def post_create_product(
    self,
    create_data: ProductCreateSchema,
    db: AsyncSession = Depends(get_db_session),
    product_service: ProductService = Depends(get_product_service),
) -> ProductSchema:
    product = await self.product_service.create_product(
        create_data=create_data,
        db=db
    )

    return product

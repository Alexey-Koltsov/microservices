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
    response_model=Optional[List[ProductSchema]],
    description="Получение листинга всех продуктов",
)
async def get_all_products(
    db: AsyncSession = Depends(get_db_session),
    product_service: ProductService = Depends(get_product_service),
):
    products = await product_service.get_products_service(db=db)
    return products


@router.post(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=ProductSchema,
    description="Создание продукта",
)
async def post_create_product(
    create_data: ProductCreateSchema,
    db: AsyncSession = Depends(get_db_session),
    product_service: ProductService = Depends(get_product_service),
):
    product = await product_service.create_product_service(
        create_data=create_data,
        db=db
    )

    return product

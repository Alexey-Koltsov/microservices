from typing import List

from fastapi import APIRouter, Depends, HTTPException

from routing.schemas.product_schemas import ProductSchema, ProductCreateSchema
from application.services.product_service import ProductService
from adapters.routs.settings import create_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=List[ProductSchema],
    description="Получение листинга всех продуктов",
)
async def get_all_products(
    product_service: ProductService = Depends(create_product_service),
):
    products = await product_service.get_products()
    return products


@router.get(
    "/{product_id}",
    responses={400: {"description": "Bad request"}},
    response_model=ProductSchema,
    description="Получение продукта по id",
)
async def get_product(
    product_id: int,
    product_service: ProductService = Depends(create_product_service),
):
    product = await product_service.get_product(product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=ProductSchema,
    description="Создание продукта",
)
async def post_create_product(
    create_data: ProductCreateSchema,
    product_service: ProductService = Depends(create_product_service),
):
    product = await product_service.create_product_service(
        create_data=create_data
    )

    return product

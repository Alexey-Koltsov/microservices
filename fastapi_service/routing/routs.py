from fastapi import APIRouter, Depends, HTTPException

from routing.schemas.product_schemas import ProductSchema, ProductCreateSchema
from application.services.product_service import ProductService
from adapters.depends.product_depends import create_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=list[ProductSchema],
    description="Получение всех продуктов",
)
async def get_all_products(
    product_service: ProductService = Depends(create_product_service),
) -> list[ProductSchema]:
    """Метод для получения продуктов"""
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
) -> ProductSchema:
    """Метод для получения продукта по id"""
    product = await product_service.get_product(product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post(
    "/",
    responses={400: {"description": "Bad request"}},
    response_model=ProductSchema,
    description="Создание продукта",
    status_code=201,
)
async def post_create_product(
    create_data: ProductCreateSchema,
    product_service: ProductService = Depends(create_product_service),
) -> ProductSchema:
    """Метод для создания продукта"""
    product = await product_service.create_product_service(
        create_data=create_data
    )
    return product

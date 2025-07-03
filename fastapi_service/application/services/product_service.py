from application.interfaces.product_interface import ProductInterface
from attr import frozen

from routing.schemas.product_schemas import ProductCreateSchema, ProductSchema


@frozen
class ProductService:
    """Сервис для продукта"""
    product_repository: ProductInterface

    async def get_products(self) -> list[ProductSchema]:
        """Метод для получения продуктов"""
        results = await self.product_repository.get_products()
        return [ProductSchema(
            id=result.id,
            name=result.name,
            category_id=result.category_id,
            quantity=result.quantity
        ) for result in results]

    async def get_product(self, product_id: int) -> ProductSchema | None:
        """Метод для получения продукта по id"""
        result = await self.product_repository.get_product(
            product_id=product_id
        )
        return ProductSchema(
            id=result.id,
            name=result.name,
            category_id=result.category_id,
            quantity=result.quantity
        ) if result else None

    async def create_product_service(
        self,
        create_data: ProductCreateSchema,
    ) -> ProductSchema:
        """Метод для создания продукта"""
        result = await self.product_repository.create_product(
            create_data=create_data
        )
        return ProductSchema(
            id=result.id,
            name=result.name,
            category_id=result.category_id,
            quantity=result.quantity
        )

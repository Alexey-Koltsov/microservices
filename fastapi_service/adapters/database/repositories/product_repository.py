from fastapi import HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.database.mapping import Product

from application.interfaces.product_interface import ProductInterface
from routing.schemas.product_schemas import ProductCreateSchema


class ProductRepository(ProductInterface):
    """Репозиторий для продукта"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_products(self) -> list[Product]:
        """Метод для получения продуктов"""
        stmt = select(Product)
        results = await self.session.execute(stmt)
        products = [Product(id=result.id,
                            name=result.name,
                            category_id=result.category_id,
                            quantity=result.quantity)
                    for result in results.scalars().all()]
        return products

    async def get_product(self, product_id: int) -> Product | None:
        """Метод для получения продукта по id"""
        smt = await self.session.execute(
            select(Product)
            .where(
                Product.id == product_id
            )
        )
        result = smt.scalars().one_or_none()
        return Product(
            id=result.id,
            name=result.name,
            category_id=result.category_id,
            quantity=result.quantity
        ) if result else None

    async def create_product(
            self,
            create_data: ProductCreateSchema,
    ) -> Product:
        """Метод для создания продукта"""
        create_data_dict = create_data.dict()
        stmt = insert(Product).values(**create_data_dict).returning(Product)
        try:
            results = await self.session.execute(stmt)
            result = results.scalars().one_or_none()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        product = Product(id=result.id,
                          name=result.name,
                          category_id=result.category_id,
                          quantity=result.quantity)

        return product

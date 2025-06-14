from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    name: str
    category_id: int
    quantity: int


class ProductSchema(ProductCreateSchema):
    id: int



from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import registry, relationship


mapper_registry = registry()

category_table = Table(
    "category",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
)


class Category:
    pass


mapper_registry.map_imperatively(Category, category_table)


product_table = Table(
    "product",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(150)),
    Column("quantity", Integer),
    Column("category_id", Integer, ForeignKey("category.id")),
)


class Product:
    pass


mapper_registry.map_imperatively(
    Product,
    product_table,
    properties={
        "category_table": relationship(Category, backref="product",
                                       order_by=category_table.c.id)
    },
)

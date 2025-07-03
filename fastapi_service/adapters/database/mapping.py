from sqlalchemy.orm import registry, relationship

from adapters.database.tables import category_table, product_table
from application.dataclasses.dataclasses import Category, Product

mapper_registry = registry()

mapper_registry.map_imperatively(Category, category_table)

mapper_registry.map_imperatively(
    Product,
    product_table,
    properties={
        "category_table": relationship(Category, backref="product",
                                       order_by=category_table.c.id)
    },
)

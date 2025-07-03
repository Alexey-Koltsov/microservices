from sqlalchemy import Column, Integer, String, Table, ForeignKey, MetaData


metadata = MetaData()

category_table = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
)


product_table = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(150)),
    Column("quantity", Integer),
    Column("category_id", Integer, ForeignKey("category.id")),
)

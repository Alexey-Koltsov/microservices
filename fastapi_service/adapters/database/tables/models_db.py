from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    category = relationship("Category", back_populates="products")

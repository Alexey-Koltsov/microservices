from attr import dataclass


@dataclass
class ProductDTO:
    id: int
    name: str
    category_id: int
    quantity: int

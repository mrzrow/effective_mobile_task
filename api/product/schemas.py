from pydantic import BaseModel, ConfigDict, NonNegativeInt, NonNegativeFloat, Field


class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., max_length=32)
    description: str
    price: NonNegativeFloat
    amount: NonNegativeInt


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

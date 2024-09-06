from pydantic import BaseModel, Field


class ProductSerializer(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    description: str

    class Config:
        orm_mode=True


class ProductCreateSerializer(BaseModel):
    title: str
    price: float
    quantity: int
    description: str


class ProductUpdateSerializer(BaseModel):
    title: str
    price: float
    quantity: int
    description: str

from pydantic import BaseModel
from typing import List
from decimal import Decimal

class SalesOrderLineCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: Decimal

class SalesOrderCreate(BaseModel):
    order_number: str
    customer_id: int
    lines: List[SalesOrderLineCreate]

class SalesOrderLineResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True

class SalesOrderResponse(BaseModel):
    id: int
    order_number: str
    customer_id: int
    status: str
    lines: list[SalesOrderLineResponse]

    class Config:
        from_attributes = True
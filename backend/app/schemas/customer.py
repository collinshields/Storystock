from pydantic import BaseModel
from typing import Optional

class CustomerCreate(BaseModel):
    customer_code: str
    name: str

    email: Optional[str] = None
    phone: Optional[str] = None

    billing_address: Optional[str] = None
    shipping_address: Optional[str] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None

    email: Optional[str] = None
    phone: Optional[str] = None

    billing_address: Optional[str] = None
    shipping_address: Optional[str] = None


class CustomerResponse(BaseModel):
    id: int

    customer_code: str

    name: str

    email: Optional[str]
    phone: Optional[str]

    billing_address: Optional[str]
    shipping_address: Optional[str]

    class Config:
        from_attributes = True
from sqlalchemy import Column, Integer, String
from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_code = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255))
    phone = Column(String(50))
    billing_address = Column(String)
    shipping_address = Column(String)
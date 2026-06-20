from sqlalchemy import Column, Integer, String, Numeric
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    cost = Column(Numeric(10, 2), nullable=True)
    quantity_on_hand = Column(Integer, default=0)
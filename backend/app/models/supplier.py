from sqlalchemy import Column, Integer, String
from app.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)

    supplier_code = Column(String(50), unique=True, nullable=False)

    name = Column(String(255), nullable=False)

    email = Column(String(255))

    phone = Column(String(50))

    address = Column(String)
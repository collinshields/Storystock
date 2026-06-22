from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from app.database import Base

class SalesOrder(Base):
    __tablename__ = "sales_orders"

    id = Column(Integer, primary_key=True, index=True)

    order_number = Column(String(50), unique=True, nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    status = Column(String(20), default="OPEN")

class SalesOrderLine(Base):
    __tablename__ = "sales_order_lines"

    id = Column(Integer, primary_key=True)

    sales_order_id = Column(Integer, ForeignKey("sales_orders.id"), nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False)

    unit_price = Column(Numeric(10, 2), nullable=False)
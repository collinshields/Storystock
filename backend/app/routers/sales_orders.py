from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.sales_order import SalesOrder, SalesOrderLine
from app.schemas.sales_order import SalesOrderCreate, SalesOrderResponse

router = APIRouter(
    prefix="/sales-orders",
    tags=["Sales Orders"]
)

@router.post("/", response_model=SalesOrderResponse)
def create_sales_order(
    order: SalesOrderCreate,
    db: Session = Depends(get_db)
):
    db_order = SalesOrder(
        order_number=order.order_number,
        customer_id=order.customer_id,
        status="OPEN"
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # Create order lines
    for line in order.lines:
        db_line = SalesOrderLine(
            sales_order_id=db_order.id,
            product_id=line.product_id,
            quantity=line.quantity,
            unit_price=line.unit_price
        )
        db.add(db_line)

    db.commit()
    db.refresh(db_order)

    return db_order

@router.get("/", response_model=list[SalesOrderResponse])
def list_sales_orders(db: Session = Depends(get_db)):
    return db.query(SalesOrder).all()

@router.get("/{order_id}", response_model=SalesOrderResponse)
def get_sales_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(SalesOrder).filter(SalesOrder.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Sales order not found")

    return order
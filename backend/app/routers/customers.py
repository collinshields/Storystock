from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomerResponse)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    db_customer = Customer(**customer.model_dump())

    db.add(db_customer)

    db.commit()

    db.refresh(db_customer)

    return db_customer

@router.get("/", response_model=list[CustomerResponse])
def list_customers(
    db: Session = Depends(get_db)
):
    return db.query(Customer).all()

@router.get("/{customer_id}",
            response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

@router.put("/{customer_id}",
            response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    updates: CustomerUpdate,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    for field, value in updates.model_dump(
        exclude_unset=True
    ).items():
        setattr(customer, field, value)

    db.commit()

    db.refresh(customer)

    return customer

@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(customer)

    db.commit()

    return {"message": "Customer deleted"}
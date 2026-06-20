from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(data: dict, db: Session = Depends(get_db)):
    product = Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
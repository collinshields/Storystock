from fastapi import FastAPI
from app.database import Base, engine

# For later use in app [probably (maybe)]
from app.models.product import Product
from app.models.customer import Customer
from app.models.supplier import Supplier
from app.models.sales_order import SalesOrder

from app.routers.products import router as products_router
from app.routers.customers import router as customers_router
from app.routers.suppliers import router as suppliers_router
from app.routers.sales_orders import router as sales_orders_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Storystock")

app.include_router(products_router)
app.include_router(customers_router)
app.include_router(suppliers_router)
app.include_router(sales_orders_router)

@app.get("/")
def root():
    return {"status": "Storystock"}
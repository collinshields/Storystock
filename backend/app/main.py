from fastapi import FastAPI
from app.database import Base, engine
import app.base

from app.routers.products import router as products_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Storystock")

app.include_router(products_router)

@app.get("/")
def root():
    return {"status": "Storystock"}
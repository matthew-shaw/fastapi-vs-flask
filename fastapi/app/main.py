from app import models
from app.database import engine
from app.routers import items

from fastapi import FastAPI

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router, prefix="/v1")

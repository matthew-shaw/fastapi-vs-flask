from app.routers import items

from fastapi import FastAPI

app = FastAPI()

app.include_router(items.router, prefix="/v1")

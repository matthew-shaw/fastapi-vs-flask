from pydantic import BaseModel

from fastapi import FastAPI


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 12.3,
                    "tax": 1.23,
                }
            ]
        }
    }


app = FastAPI()


@app.post(
    "/items/",
    status_code=201,
    tags=["Item"],
)
async def create(item: Item) -> dict:
    """Create an Item"""
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/{item_id}", tags=["Item"])
async def get(item_id: int, q: str | None = None) -> dict:
    """Get an Item"""
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.put(
    "/items/{item_id}",
    tags=["Item"],
)
async def update(item_id: int, item: Item) -> dict:
    """Update an Item"""
    return {"item_id": item_id, **item.dict()}

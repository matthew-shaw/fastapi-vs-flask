from app.models import Item

from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])


@router.post(
    "/",
    status_code=201,
)
async def create(item: Item) -> dict:
    """Create an Item"""
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@router.get("/{item_id}")
async def get(item_id: int, q: str | None = None) -> dict:
    """Get an Item"""
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@router.put("/{item_id}")
async def update(item_id: int, item: Item) -> dict:
    """Update an Item"""
    return {"item_id": item_id, **item.dict()}

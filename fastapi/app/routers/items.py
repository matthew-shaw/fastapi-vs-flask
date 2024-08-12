from app import crud, schemas
from app.dependencies import get_db
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/items",
    tags=["Items"],
    dependencies=[Depends(get_db)],
)


@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create an item.
    """
    return crud.create_item(db, item=item)


@router.get("/", response_model=list[schemas.Item])
def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """
    List items.
    """
    items = crud.list_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get an item.
    """
    return crud.get_item(db, item_id=item_id)


@router.put("/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, db: Session = Depends(get_db)):
    """
    Update an item.
    """
    return crud.update_item(db, item_id=item_id)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item.
    """
    return crud.delete_item(db, item_id=item_id)

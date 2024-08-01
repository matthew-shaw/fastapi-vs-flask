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
    return crud.create_item(db, item=item)


@router.get("/", response_model=list[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

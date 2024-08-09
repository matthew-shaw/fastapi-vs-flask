from app import models, schemas
from sqlalchemy.orm import Session


def get_item(db: Session, item_id: int) -> models.Item | None:
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100) -> list[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(
    db: Session,
    item: schemas.ItemCreate,
) -> models.Item:
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

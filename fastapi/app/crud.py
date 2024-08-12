from app import models, schemas
from sqlalchemy.orm import Session


def get_item(db: Session, item_id: int) -> models.Item | None:
    """
    Get an item.
    """
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def list_items(db: Session, skip: int = 0, limit: int = 100) -> list[models.Item]:
    """
    List items.
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(
    db: Session,
    item: schemas.ItemCreate,
) -> models.Item:
    """
    Create an item.
    """
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int) -> models.Item | None:
    """
    Update an item.
    """
    return None


def delete_item(db: Session, item_id: int) -> None:
    """
    Delete an item.
    """
    return None

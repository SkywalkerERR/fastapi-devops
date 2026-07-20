# items.py - API endpoints for items

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.item import Item

from datetime import datetime

# Теперь все эндпоинты автоматически получат префикс /items.
router = APIRouter(prefix="/items", tags=["items"])

# Pydantic-схема для создания нового элемента
# Она будет использоваться для валидации данных при создании нового элемента
# Она определяет, что для создания нового элемента нужно передать только name и description
# Используется при получении данных от клиента.
class ItemCreate(BaseModel):
    name: str
    description: str

# Pydantic-схема для чтения элемента
# Она будет использоваться для чтения данных о элементе
# Она определяет, что для чтения элемента нужно передать только id, name, description и created_at
# Используется при возврате данных клиенту.
class ItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True) # Это позволяет FastAPI автоматически преобразовать данные из базы данных в Pydantic-модель.
    id: int
    name: str
    description: str | None
    created_at: datetime

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    item = Item(name=payload.name, description=payload.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/", response_model=list[ItemRead])
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).order_by(Item.id).all() # Получаем все элементы из базы данных и возвращаем их в виде списка.


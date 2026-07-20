#session.py - это место, где мы определяем сессию для работы с БД.

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings


engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)      # sessionmaker - это фабрика для создания сессий

def get_db() -> Generator[Session, None, None]:      # Generator - это генератор, который возвращает сессию
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
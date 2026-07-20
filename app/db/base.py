#base.py - это место, где мы определяем базовый класс для всех моделей.

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):      # DeclarativeBase - это базовый класс для всех моделей, который предоставляет основные функции для работы с моделями
    '''Базовый класс для всех моделей'''
    pass
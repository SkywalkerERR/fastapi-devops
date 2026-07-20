# Запуск для проверки:
#   uvicorn app.main:app --reload

from fastapi import Depends, FastAPI, status
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

# Импортируем router из items.py
from app.api.items import router as items_router
from app.db.session import get_db

app = FastAPI(title="fastapi-devops")

# Регистрируем router в FastAPI
app.include_router(items_router)



@app.get("/")
def root():
    return {"service": "fastapi-devops", "status": "running"}


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "ok"}
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "unhealthy", "database": "unavailable"},
        )
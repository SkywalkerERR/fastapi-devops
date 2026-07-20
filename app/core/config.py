#config.py - это место, где приложение получает все настройки из окружения (.env или Docker environment).

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Имена полей = имена переменных окружения (DB_HOST, DB_PORT, ...)

    DB_HOST: str
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    model_config = SettingsConfigDict(          # Если есть .env, загрузи его автоматически
        env_file = ".env",      # удобно при локальном запуске без Docker
        env_file_encoding = "utf-8",
        extra = "ignore",       # не будет ошибки, если переменных окружения нет
    )

    @property
    def database_url(self) -> str:      # строка для подключения к БД postgresql://admin:password@postgres:5432/fastapi_db
        return(
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()
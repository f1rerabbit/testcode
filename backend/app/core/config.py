from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "AI Video Factory API"

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "ai_video_factory"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"

    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "change-me"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


settings = Settings()

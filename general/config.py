from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_name: str = Field(..., alias="DB_NAME")
    db_user: str = Field(..., alias="DB_USER")
    db_password: str = Field(..., alias="DB_PASSWORD")
    db_host: str = Field(..., alias="DB_HOST")
    db_port: int = Field(..., alias="DB_PORT")
    secret_key: str = Field(..., alias="SECRET_KEY")
    debug: bool = Field(..., alias="DEBUG")

    model_config = SettingsConfigDict(env_file=".env", populate_by_name=True)


settings = Settings()

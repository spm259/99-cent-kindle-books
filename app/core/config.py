from pydantic import BaseSettings

class Settings(BaseSettings):
    amazon_api_key: str
    amazon_api_secret: str

    class Config:
        env_file = ".env"

settings = Settings()

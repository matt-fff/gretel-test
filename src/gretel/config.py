import os

from pydantic import BaseSettings


class Config(BaseSettings):
    api_key: str

    class Config:
        case_sensitive=False
        env_file=os.environ.get("ENVFILE", ".env")
        env_file_encoding="utf-8"
        env_nested_delimiter="__"


conf = Config()

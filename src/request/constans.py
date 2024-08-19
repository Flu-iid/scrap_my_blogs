from src.config.config import Config
from app import config_path

config = Config(config_path)

URLS: str = config.url_path

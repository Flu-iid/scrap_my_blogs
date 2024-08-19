from sys import argv
from src.config.config import Config

# handle argv
name, *values = argv

config_path: str = ""


def init(val):
    conf = Config(val)


if __name__ == "__main__":
    pass

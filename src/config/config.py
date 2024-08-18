from configparser import ConfigParser
import exceptions as e
import os


class Config:
    def __init__(self, config_path: str) -> None:
        self.config_path = config_path
        self.config = ConfigParser()
        self.check_file_existance()
        self.list = self.read()

    def check_file_existance(self) -> bool:
        @e.pathError
        def path_error():
            return os.path.isfile(self.config_path)

        return path_error()

    def read(self) -> list:
        @e.parsingError
        def parse_error():
            return self.config.read(self.config_path)

        return parse_error()


if __name__ == "__main__":
    conf = Config("config.ini")

from configparser import ConfigParser
import exceptions as e
import os

class Parser:
    def __init__(self, config_path: str) -> None:
        self.config_path = config_path
        self.parser = ConfigParser()

    def 

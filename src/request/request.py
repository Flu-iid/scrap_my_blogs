from src.request import constans as rc
import requests


class Request:
    def __init__(self) -> None:
        self.url_path: str = rc.URLS
        self.urls: list = []
        self.read_urls()

    def read_urls(self):
        with open(self.url_path, "r") as fin:
            urls = fin.readlines()
            for u in urls:
                self.urls.append(u.strip())

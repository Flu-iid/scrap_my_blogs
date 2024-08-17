class Check:
    def __init__(self, page_count: bool, config_path: str, urls_path: str) -> None:
        self.page_count_flag: bool = page_count
        self.config_path: str = config_path
        self.urls_path: str = urls_path

    def config(self):
        pass

    def urls(self):
        pass

    def connection(self):
        # add flag for like number of pages to check
        pass

    def save_location(self):
        pass

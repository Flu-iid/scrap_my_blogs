from configparser import ConfigParser
import exceptions as e
from os import path, get_terminal_size


class Config:
    def __init__(self, config_path: str, verbose: bool = False) -> None:
        self.config_path = config_path
        self.config = ConfigParser()
        self.terminal_width = get_terminal_size()[0]
        self.config_path_exist = self.check_file_existance()
        self.config_name = self.read() if self.config_path_exist else None
        self.map_values_status = self.map_values() if self.config_name else None
        if verbose:
            self.show()

    def check_file_existance(self) -> bool:
        @e.pathError
        def path_error():
            return path.isfile(self.config_path)

        return path_error()

    def read(self) -> list[str] | None:
        @e.parsingError
        def parse_error():
            return self.config.read(self.config_path)

        return parse_error()

    def map_values(self) -> int:
        @e.configValueError
        def value_error():
            scraper = self.config["SCRAPER"]
            url_path = self.config["URL_PATH"]
            save_path = self.config["SAVE_PATH"]
            # attributes = self.config["ATTRBUTES"]

            self.parser = scraper["parser"]
            self.method = scraper["method"]
            self.page_count = scraper["page_count"]

            self.url_path = url_path["path"]

            self.save_path = save_path["path"]

        return value_error()

    def show(self):
        """
        add detail to show on verbose mode
        """

        message: str = f"\n\
config path status: {'ok' if self.config_path_exist else 'error'}\n\
config read status: {'ok' if self.config_name else 'error'}\n\
config name: {self.config_name[0] if self.config_name else ''}\n\
config value status: {'ok' if self.map_values_status else 'error'}\n"
        if self.map_values_status:
            config_values_message = f"\
__config\n\
________parser: {self.parser}\n\
________method: {self.method}\n\
________page count: {self.page_count}\n\
________url path: {self.url_path}\n\
________save path: {self.save_path}\n\
{'-'*self.terminal_width}"

        message += config_values_message

        print(message)


if __name__ == "__main__":
    conf = Config("config.ini", verbose=True)
    print()

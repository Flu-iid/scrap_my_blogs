import requests
from bs4 import BeautifulSoup as bs
import os


class Mod:
    def __init__(self, parser: str = "lxml", url_file_path: str = "urls") -> None:
        self.parser: str = parser
        self.url_file_path: str = url_file_path
        self.urls: list = []
        self.add_url()

    def add_url(self) -> None:
        with open(self.url_file_path, "r") as fin:
            urls = fin.readlines()
            for u in urls:
                self.urls.append(u.strip())

    def make_bs(self, request: requests.Response) -> bs:
        return bs(request.content, features=self.parser)

    def page_count(self, url) -> int:
        page_request = requests.get(url)
        last_page_bs = self.make_bs(page_request)
        page_count_element = last_page_bs.find(attrs={"class": "last"})
        count = page_count_element.contents[0]

        # make site dir on check

        return int(count)

    def page_articles(self, url: str) -> list[str]:
        page_request = requests.get(url)
        page_bs = self.make_bs(page_request)
        find = page_bs.find_all(attrs={"class": "more-link"})
        return [i["href"] for i in find]

    def image_pair_values(self, url: str) -> tuple[str, str]:
        """
        return (title, half url)
        half url to start from image 0 till fail
        """
        page_request = requests.get(url)
        page_bs = self.make_bs(page_request)
        title = url.split("/")[-2]
        first_img = page_bs.find(attrs={"class": "alignnone"})
        empty_url = first_img["src"][:-15]
        return title, empty_url

    def scrap_and_save(self, title: str, half_url: str) -> None:
        count = 0
        while True:
            count += 1
            response = requests.get(half_url + f"{count:03}.jpg")
            if response.headers["Content-Type"] != "image/jpeg":
                print(f"END of {title} || count:{count-1}")
                return 1
            # os.getcwd()
            # os.mkdir(os.path.join(".", f"{title}"))
            with open(f"./src/xblog/{title}-{count:03}.jpg", "wb") as fout:
                fout.write(response.content)
            print(title, count)


if __name__ == "__main__":
    # a = requests.get("https://gravureblog.tv/")
    # my_bs = bs(a.content, features="lxml")
    # with open("output", "w") as fout:
    #     fout.write(my_bs.prettify())
    # result = my_bs.find(attrs={"class": "last"})

    # print(result.contents[0])

    a = Mod()
    print(a.urls)
    # gravure = a.urls[0]
    # print(a.page_count(gravure))
    t, u = a.image_pair_values("https://xblog.tv/masha-juventa-club-red-2/")
    a.scrap_and_save(t, u)

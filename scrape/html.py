import requests
from bs4 import BeautifulSoup
from scrape.query_builder import QueryBuilder
from functools import partial
import re


def extract_field(post, pattern: str = ""):
    pattern = re.compile(pattern, re.IGNORECASE)
    for field in post.find_all("b"):
        value = field.find(string=pattern)
        if value:
            return str(value.next_element).strip()


def extract_info(url: str, mods: list[callable] = []) -> list[list]:
    soup = _soupify(url)
    for post in _get_postings(soup):
        yield [mod(post) for mod in mods]


# private methods


def _soupify(url: str) -> BeautifulSoup:
    page = requests.get(url)
    return BeautifulSoup(page.text)


def _get_postings(soup: BeautifulSoup):
    for posting in soup.find_all(class_="bsitem"):
        yield posting


if __name__ == "__main__":
    base_url = "https://www.pinkbike.com/buysell/list"
    url = QueryBuilder(base_url).add_query("category", 2).build()
    get_material = partial(extract_field, pattern="material")
    get_condition = partial(extract_field, pattern="condition")
    get_wheel_size = partial(extract_field, pattern="wheel size")
    get_rear_travel = partial(extract_field, pattern="rear travel")
    get_front_travel = partial(extract_field, pattern="front travel")
    mods = [
        extract_field,
        get_wheel_size,
        get_material,
        get_front_travel,
        get_rear_travel,
    ]
    gen = extract_info(url, mods)
    res = next(gen)
    print(res)

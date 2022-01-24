from bs4 import BeautifulSoup
import re
from scrape.utils import to_dict


def get_title(post):
    title = post.select("tr > td > div > a")
    return ("title", title and title[0].text)


def get_price(post):
    pattern = re.compile(r"\$[1-9][0-9]*\s[A-Z]{3}")
    price = post.find_all("b", string=pattern)
    return ("price", price and price[0].text)


def get_spec(post, text: str = ""):
    pattern = re.compile(text, re.IGNORECASE)
    field = post.find("b", string=pattern)
    value = str(field.next_element.next_element).strip() if field else None
    return (text, value)


def get_postings(soup: BeautifulSoup):
    for posting in soup.find_all(class_="bsitem"):
        yield posting


def scrape_page(page: BeautifulSoup, mods: list[callable] = []) -> list[list]:
    for post in get_postings(page):
        yield to_dict([mod(post) for mod in mods])

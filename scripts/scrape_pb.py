from scrape.query_builder import QueryBuilder
import requests
from bs4 import BeautifulSoup
from scrape.html import get_title, get_price, scrape_page

base_url = "https://www.pinkbike.com/buysell/list"
qb = QueryBuilder(base_url)
qb.upsert_query("category", 2)
qb.upsert_query("page", 1)

page = requests.get(qb.build())
soup = BeautifulSoup(page.text)

result = list(scrape_page(soup, mods=[get_title, get_price]))
print(result)

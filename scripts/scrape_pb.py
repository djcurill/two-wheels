from scrape.query_builder import QueryBuilder
from scrape.html import get_title, get_price
from app.constants import BikeCategory
from scrape.crawler import PbCrawler


base_url = "https://www.pinkbike.com/buysell/list/"
qb = QueryBuilder(base_url)
qb.upsert_query("category", BikeCategory.ENDURO.value)
mods = [get_title, get_price]

crawler = PbCrawler(qb, mods)
gen = crawler.scrape_current_page()
print(next(gen))

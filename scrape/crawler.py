from scrape.exceptions import SoupifyException
from scrape.query_builder import QueryBuilder
from scrape.html import scrape_page
from scrape.utils import soupify
from functools import partial
import time


class PbCrawler:
    """
    Crawls pinkbike.com buy/sell pages for mountain bike data

    Attributes:
        qb: QueryBuilder, builds query for current page and given query parameters
        mods: list[callable], retrieves data from BeautifulSoup nodes

    """

    def __init__(self, qb: QueryBuilder, mods: list[callable], start: int = 1):
        self.qb = qb
        self.mods = mods
        self._scraper = partial(scrape_page, mods=mods)
        self.page = start
        self.qb.upsert_query("page", self.page)

    @property
    def current_url(self):
        return self.qb.build()

    def increment_page(self):
        self.page += 1
        self.qb.upsert_query("page", self.page)

    def scrape_current_page(self):
        soup = soupify(self.current_url)

        if soup is None:
            raise SoupifyException(self.current_url)

        for data in self._scraper(soup):
            yield data

    def crawl(self, n: int, patience: float):
        for _ in range(n):
            for data in self.scrape_current_page():
                yield data
            time.sleep(patience)
            self.increment_page()

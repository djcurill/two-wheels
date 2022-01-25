from scrape.query_builder import QueryBuilder
import pytest


@pytest.fixture()
def base_url():
    return "http://testurl.com/"


def test_base_url(base_url):
    qb = QueryBuilder(base_url)
    assert qb.base_url == base_url


def test_base_url_appends_forward_slash():
    base_url = "http://testurl.com"
    qb = QueryBuilder(base_url)
    assert qb.base_url == base_url + "/"


def test_edit_existing_query(base_url):
    qb = QueryBuilder(base_url)
    qb.upsert_query("int_query", 1)
    qb.upsert_query("int_query", 2)
    result = qb.build()
    assert result == f"{base_url}?int_query=2"


def test_single_query(base_url):
    result = QueryBuilder(base_url).upsert_query("int_query", 1).build()
    assert result == f"{base_url}?int_query=1"


def test_multiple_queries(base_url):
    result = (
        QueryBuilder(base_url)
        .upsert_query("int_query_one", 1)
        .upsert_query("int_query_two", 2)
        .build()
    )
    assert result == f"{base_url}?int_query_one=1&int_query_two=2"


def test_contains_query(base_url):
    result = QueryBuilder(base_url).upsert_query("contains", [1, 2]).build()
    assert result == f"{base_url}?contains=1,2"

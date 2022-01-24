from bs4 import BeautifulSoup
from functools import partial
from scrape.html import get_title, get_price, get_spec, get_postings, scrape_page


def create_post(
    title: str = "",
    condition: str = "",
    wheel_size: str = "",
    price: float = 0,
    currency: str = "CAD",
) -> str:
    return f"""
    <div class='bsitem'>
        <table>
            <tbody>
                <tr>
                    <td><p>Photos</p></td>
                    <td>
                        <div>
                            <a href='http://road.to.nowhere'>{title}</a>
                            <div>
                                <b>Condition: </b> {condition}
                            </div>
                            <div>
                                <b>Wheel size: </b> {wheel_size}
                            </div>
                        </div>
                        <table>
                            <tbody>
                                <tr>
                                    <td>
                                        <b>${price} {currency}</b>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    """


def create_posts():
    posts = [
        create_post(title="Bike One", condition="good", price=2000),
        create_post(title="Bike Two", condition="bad", price=1000),
    ]
    page = ""
    for post in posts:
        page += f"<div>\n{post}\n</div>"
    return page


def test_get_title():
    post = create_post(title="2020 Evil Following")
    soup = BeautifulSoup(post, "html.parser")
    result = get_title(soup)
    assert result[1] == "2020 Evil Following"


def test_get_price():
    post = create_post(price=4500, currency="CAD")
    soup = BeautifulSoup(post, "html.parser")
    result = get_price(soup)
    assert result[1] == "$4500 CAD"


def test_extract_field():
    post = create_post(condition="very good")
    soup = BeautifulSoup(post, "html.parser")
    result = get_spec(soup, text="condition")
    assert result[1] == "very good"


def test_get_postings():
    page = create_posts()
    soup = BeautifulSoup(page, "html.parser")
    posts = list(get_postings(soup))
    assert len(posts) == 2


def test_scrape_page():
    page = create_posts()
    page = BeautifulSoup(page, "html.parser")
    mods = [get_title, get_price, partial(get_spec, text="condition")]
    result = list(scrape_page(page, mods))
    assert len(result) == 2
    assert result[0]["title"] == "Bike One"
    assert result[0]["price"] == "$2000 CAD"
    assert result[0]["condition"] == "good"
    assert result[1]["title"] == "Bike Two"
    assert result[1]["price"] == "$1000 CAD"
    assert result[1]["condition"] == "bad"

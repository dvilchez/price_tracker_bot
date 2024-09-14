from infra.price import Prices


def test_scrape_amazon_price_e2e(monkeypatch):
    price = Prices().get_price("https://www.amazon.es/dp/B0CC8SJCTT")
    assert price is not None

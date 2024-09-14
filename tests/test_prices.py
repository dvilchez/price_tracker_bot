import requests
from price import Prices


def test_scrape_amazon_price(monkeypatch):
    class MockResponse:
        @staticmethod
        def get(url, headers):
            class MockContent:
                content = '''
                <html>
                    <span id="priceblock_ourprice">$19.99</span>
                </html>
                '''
            return MockContent()

    monkeypatch.setattr(requests, "get", MockResponse.get)
    price = Prices().get_price("https://www.amazon.com/dp/test")
    assert price == "19.99"

import requests
import re


class Prices:
    def scrape_amazon_price(self, url):
        from bs4 import BeautifulSoup

        headers = {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                           "AppleWebKit/537.36 (KHTML, like Gecko)",
                           "Chrome/58.0.3029.110 Safari/537.3")
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        price_text = soup.find("span", "aok-offscreen").get_text()
        match = re.search(r'[\d,.]+', price_text)
        if match:
            return match.group()
        return None

    def get_price(self, product_url):
        return self.scrape_amazon_price(product_url)

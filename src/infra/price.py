from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time


class Prices:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" +
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/" +
            "605.1.15(KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/" +
            "20100101 Firefox/89.0",
        ]
        chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

        self.service = Service()
        self.driver = webdriver.Chrome(
            service=self.service, options=chrome_options)

    def mimic_human_behavior(self):
        time.sleep(random.uniform(2, 5))

    def scrape_amazon_price(self, url):
        price_selectors = [
            "span.a-price-whole",
            "span.a-price-fraction"
        ]
        price_whole = None
        price_fraction = None

        self.driver.get(url)
        self.mimic_human_behavior()
        try:
            for selector in price_selectors:
                if "whole" in selector:
                    price_whole = self.driver.find_element(
                        By.CSS_SELECTOR, selector).text
                else:
                    price_fraction = self.driver.find_element(
                        By.CSS_SELECTOR, selector).text

            if price_whole and price_fraction:
                return float(f"{price_whole}.{price_fraction}")
        except Exception:
            return None

        return None

    def get_price(self, product_url):
        return self.scrape_amazon_price(product_url)

    def __del__(self):
        self.driver.quit()

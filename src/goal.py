import validators
from price import Prices


class Tracking:
    def __init__(self, user_id, product_url, goal):
        if not validators.url(product_url):
            raise ValueError("Must be a valid URL")

        if not isinstance(goal, (int, float)):
            raise ValueError("Must be a valid GOAL")

        self.user_id = user_id
        self.product_url = product_url
        self.goal = goal


class GoalChecker:
    def __init__(self, prices):
        self.prices = prices

    def check_goal(self, tracking):
        price = self.prices.get_price(tracking.product_url)
        return price <= tracking.goal


prices = Prices()
tracker = GoalChecker(prices)


def check_goal(tracking):
    if tracker.check_goal(tracking):
        price = prices.get_price(tracking.product_url)
        return price, True

    return None, False

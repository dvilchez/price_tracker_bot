from infra.price import Prices
from model.goal import GoalChecker

prices = Prices()
tracker = GoalChecker()


def check_goal(tracking):
    current_price = prices.get_price(tracking.product_url)
    if tracker.check_goal(tracking, current_price):
        return current_price, True

    return None, False

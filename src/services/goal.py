from infra.price import Prices
from model.goal import GoalChecker

prices = Prices()
tracker = GoalChecker(prices)


def check_goal(tracking):
    if tracker.check_goal(tracking):
        price = prices.get_price(tracking.product_url)
        return price, True

    return None, False

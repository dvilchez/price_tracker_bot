import validators


class Tracking:
    def __init__(self, user_id, product_url, goal):
        if not validators.url(product_url):
            raise ValueError("Must be a valid URL")

        self.user_id = user_id
        self.product_url = product_url
        self.goal = goal


class GoalChecker:
    def __init__(self, prices):
        self.prices = prices

    def check_goal(self, tracking):
        price = self.prices.get_price(tracking.product_url)
        return price < tracking.goal

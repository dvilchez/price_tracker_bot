class Tracking:
    def __init__(self, user_id, product_id, goal):
        self.user_id = user_id
        self.product_id = product_id
        self.goal = goal


class GoalChecker:
    def __init__(self, prices):
        self.prices = prices

    def check_goal(self, tracking):
        price = self.prices.get_price(tracking.product_id)
        return price < tracking.goal


def test_check_goal():
    class MockPrices:
        def get_price(self, product_id):
            return 2

    prices = MockPrices()
    tracking = Tracking("any_user", "any_product", 3)
    checker = GoalChecker(prices)

    assert checker.check_goal(tracking) is True

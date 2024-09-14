class Goal:
    def __init__(self, user_id, product_id, goal):
        self.user_id = user_id
        self.product_id = product_id
        self.goal = goal


class GoalChecker:
    def __init__(self, prices):
        self.prices = prices

    def check_goal(self, goal):
        price = self.prices.get_price(goal.product_id)
        return price < goal.goal


def test_goal_checker():
    class MockPrices:
        def get_price(self, product_id):
            return 2

    prices = MockPrices()
    goal = Goal("any_user", "any_product", 3)
    checker = GoalChecker(prices)

    assert checker.check_goal(goal) is True

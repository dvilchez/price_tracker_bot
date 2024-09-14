from goal import Tracking, GoalChecker


def test_check_goal():
    class MockPrices:
        def get_price(self, product_url):
            return 2

    prices = MockPrices()
    tracking = Tracking("any_user", "http://shop.com/any-product", 3)
    checker = GoalChecker(prices)

    assert checker.check_goal(tracking) is True

import validators


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
    def check_goal(self, tracking, current_price):
        return current_price <= tracking.goal

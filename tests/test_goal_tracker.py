from model.goal import Tracking, GoalChecker


def test_goal_tracker_check_goal():
    tracking = Tracking("any_user", "http://shop.com/any-product", 3)
    checker = GoalChecker()

    assert checker.check_goal(tracking, 3) is True

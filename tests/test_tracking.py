import pytest
from goal import Tracking


def test_tracking_created_with_invalid_url():
    with pytest.raises(ValueError, match="Must be a valid URL"):
        Tracking("any_user", "invalid_url", 3)


def test_tracking_created_with_valid_goal():
    with pytest.raises(ValueError, match="Must be a valid GOAL"):
        Tracking("any_user", "http://anyshop.com/anyproduct", "a")

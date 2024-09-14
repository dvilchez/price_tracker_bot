import pytest
from goal import Tracking


def test_tracking_created_with_invalid_url():
    with pytest.raises(ValueError, match="Must be a valid URL"):
        Tracking("any_user", "invalid_url", 3)

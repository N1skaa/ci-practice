import random

import pytest


@pytest.mark.quarantine
def test_unstable_response_time():
    assert random.random() > 0.33
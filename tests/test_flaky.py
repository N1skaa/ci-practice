import random

import pytest

def test_unstable_response_time():
    assert random.random() > 0.33
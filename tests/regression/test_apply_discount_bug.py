"""
Regression test: catches the original bug where `apply_discount(price, percent)`
treated `percent` as a decimal instead of a percentage (e.g., 10 -> 0.10).
On the buggy version, the first assert would have failed (returned -900.0).
"""

import pytest
from src.pricing import apply_discount

def test_apply_discount_regression_single():
    # expected: 10% off 100 = 90.0
    assert apply_discount(100.0, 10) == 90.0

@pytest.mark.parametrize(
    "price, pct, expected",
    [
        (80.0, 0, 80.0),
        (200.0, 25, 150.0),
        (49.99, 10, 44.991),  # exact math; rounding (if any) is done by caller
    ],
)
def test_apply_discount_regression_more(price, pct, expected):
    assert apply_discount(price, pct) == expected

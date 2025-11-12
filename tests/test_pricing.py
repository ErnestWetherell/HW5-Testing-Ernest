import math
import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

def test_parse_price_basic():
    assert parse_price("$1,234.50") == 1234.50
    assert parse_price("12.5") == 12.5
    assert parse_price("1,000") == 1000.0

def test_format_currency():
    assert format_currency(12) == "$12.00"
    assert format_currency(12.345) == "$12.35"

def test_apply_discount_math():
    assert apply_discount(100.0, 10) == 90.0
    assert apply_discount(80.0, 0) == 80.0

def test_apply_discount_negative():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5)

def test_add_tax_and_bulk_total():
    assert math.isclose(add_tax(100.0, 0.1), 110.0, rel_tol=1e-12)
    total = bulk_total([10, 10], discount_percent=10, tax_rate=0.1)
    assert math.isclose(total, 19.8, rel_tol=1e-9)

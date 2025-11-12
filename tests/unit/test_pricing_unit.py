import math
import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

# ---------- fixtures ----------
@pytest.fixture
def sample_prices():
    # simple list for bulk_total tests
    return [1.00, 2.50, 10.00]  # subtotal = 13.50

# ---------- parse_price ----------
@pytest.mark.parametrize(
    "raw, expected",
    [
        ("$1,234.50", 1234.50),
        ("12.5", 12.5),
        ("$0.99", 0.99),
        ("1,000", 1000.0),
    ],
)
def test_parse_price_valid(raw, expected):
    assert parse_price(raw) == expected

@pytest.mark.parametrize(
    "raw",
    ["", "abc", "$", "12,34,56", " $ "]
)
def test_parse_price_invalid(raw):
    with pytest.raises(ValueError):
        parse_price(raw)

# ---------- format_currency ----------
@pytest.mark.parametrize(
    "value, expected",
    [
        (12, "$12.00"),
        (12.345, "$12.35"),
        (0, "$0.00"),
        (999.999, "$1000.00"),
    ],
)
def test_format_currency_rounding_and_format(value, expected):
    assert format_currency(value) == expected

# ---------- apply_discount ----------
@pytest.mark.parametrize(
    "price, pct, expected",
    [
        (100.0, 0, 100.0),   # 0%
        (200.0, 50, 100.0),  # large %
        (80.0, 10, 72.0),
    ],
)
def test_apply_discount_ok(price, pct, expected):
    assert apply_discount(price, pct) == expected

def test_apply_discount_negative_raises():
    with pytest.raises(ValueError):
        apply_discount(100.0, -1)

# ---------- add_tax ----------
def test_add_tax_default_zero_is_no_change():
    assert math.isclose(add_tax(100.0, 0.0), 100.0, rel_tol=1e-12)

def test_add_tax_custom_positive_rate():
    assert math.isclose(add_tax(100.0, 0.0825), 108.25, rel_tol=1e-12)

def test_add_tax_negative_raises():
    with pytest.raises(ValueError):
        add_tax(100.0, -0.01)

# ---------- bulk_total ----------
def test_bulk_total_simple_list(sample_prices):
    # subtotal = 13.50; 10% off -> 12.15; +8% tax -> 13.122
    total = bulk_total(sample_prices, discount_percent=10, tax_rate=0.08)
    assert math.isclose(total, 13.122, rel_tol=1e-12)

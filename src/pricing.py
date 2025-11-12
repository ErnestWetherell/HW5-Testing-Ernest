import re

def parse_price(s):
    s = s.strip()
    # valid: $1,234.50 | 12.5 | 0.99 | 1,000 | 123
    pattern = r'^\$?\s*(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\s*$'
    if not re.match(pattern, s):
        raise ValueError("invalid price format")
    cleaned = s.replace("$", "").replace(",", "")
    return float(cleaned)

def format_currency(v):
    return f"${v:.2f}"

def apply_discount(price, percent):
    if percent < 0:
        raise ValueError("percent must be >= 0")
    return price - price * (percent / 100.0)

def add_tax(price, rate):
    if rate < 0:
        raise ValueError("rate must be >= 0")
    return price * (1 + rate)

def bulk_total(prices, discount_percent=0.0, tax_rate=0.0):
    subtotal = sum(prices)
    discounted = apply_discount(subtotal, discount_percent)
    return add_tax(discounted, tax_rate)

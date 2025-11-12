def parse_price(s):
    s = s.strip().replace("$", "").replace(",", "")
    return float(s)

def format_currency(v):
    return f"${v:.2f}"

def apply_discount(price, percent):
    if percent < 0:
        raise ValueError("percent must be >= 0")
    return price - price * (percent / 100.0)

def add_tax(price, rate):
    return price * (1 + rate)

def bulk_total(prices, discount_percent=0.0, tax_rate=0.0):
    subtotal = sum(prices)
    discounted = apply_discount(subtotal, discount_percent)
    return add_tax(discounted, tax_rate)

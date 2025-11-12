from src.pricing import parse_price, format_currency, bulk_total

def load_order(path):
    items = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError("Expected two fields per line: name,price")
            name, price_str = parts
            price = parse_price(price_str)
            items.append((name.strip(), price))
    return items

def write_receipt(path, items, discount_percent=0.0, tax_rate=0.0):
    prices = [p for _, p in items]
    total = bulk_total(prices, discount_percent, tax_rate)
    with open(path, "w") as f:
        for name, price in items:
            f.write(f"{name}: {format_currency(price)}\n")
        f.write(f"TOTAL: {format_currency(total)}\n")

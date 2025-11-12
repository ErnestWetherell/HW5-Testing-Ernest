from src.order_io import load_order, write_receipt
from src.pricing import bulk_total, format_currency
import pytest

def test_load_order_happy_path(tmp_path):
    p = tmp_path / "order.csv"
    p.write_text("Widget,$10.00\nGadget,5\n\n")
    assert load_order(str(p)) == [("Widget", 10.0), ("Gadget", 5.0)]

def test_load_order_malformed(tmp_path):
    p = tmp_path / "bad.csv"
    p.write_text("bad_line_only\n")
    with pytest.raises(ValueError):
        load_order(str(p))

def test_write_receipt(tmp_path):
    items = [("Widget", 10.0), ("Gadget", 5.0)]
    out = tmp_path / "receipt.txt"
    write_receipt(str(out), items, discount_percent=10, tax_rate=0.1)

    text = out.read_text().splitlines()
    assert text[0] == "Widget: $10.00"
    assert text[1] == "Gadget: $5.00"
    expected_total = format_currency(
        bulk_total([10.0, 5.0], discount_percent=10, tax_rate=0.1)
    )
    assert text[-1] == f"TOTAL: {expected_total}"

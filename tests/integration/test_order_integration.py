import math
from src.order_io import load_order, write_receipt
from src.pricing import bulk_total, format_currency

def test_order_integration(tmp_path):
    # 1. Create a temporary CSV file
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    # 2. Load items using your function
    items = load_order(input_file)

    # 3. Compute the total using bulk_total
    prices = [p for _, p in items]
    expected_total = bulk_total(prices, discount_percent=10, tax_rate=0.1)

    # 4. Write the receipt to another temp file
    output_file = tmp_path / "receipt.txt"
    write_receipt(output_file, items, discount_percent=10, tax_rate=0.1)

    # 5. Read and verify contents
    output_text = output_file.read_text(encoding="utf-8")

    # Check each line item is in the receipt
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text

    # Check the TOTAL line exists and is formatted correctly
    expected_total_str = format_currency(expected_total)
    assert f"TOTAL: {expected_total_str}" in output_text

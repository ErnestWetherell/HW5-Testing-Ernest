# Coverage Analysis

- Command run: `pytest --cov=src --cov-report=term-missing`
- Test suite: unit + integration + regression (30 tests total).

## Raw coverage output
```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.0.1, pluggy-1.6.0
rootdir: /home/ernest/HW5-Testing-Ernest
configfile: pytest.ini
plugins: cov-7.0.0
collected 34 items

tests/integration/test_order_integration.py .                            [  2%]
tests/regression/test_apply_discount_bug.py ....                         [ 14%]
tests/test_order_io.py ...                                               [ 23%]
tests/test_pricing.py .....                                              [ 38%]
tests/unit/test_pricing_unit.py .....................                    [100%]

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src/__init__.py       0      0   100%
src/order_io.py      22      0   100%
src/pricing.py       22      0   100%
-----------------------------------------------
TOTAL                44      0   100%
============================== 34 passed in 0.08s ==============================
```

## Notes
- **Uncovered lines/functions:** (if any are shown above, list them here).
- **Acceptable gaps:** briefly justify any lines that are okay to leave uncovered (e.g., impossible branches, defensive checks).
- **Improvements:** if gaps exist, mention which tests you would add (e.g., extra malformed lines for `load_order`, additional percent/edge cases for `apply_discount`, etc.).

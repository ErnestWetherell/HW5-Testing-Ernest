# Homework
- Name: Ernest Wetherell

## Question 1) Define the following unit, integration, regression tests and when you would use each?

- **Unit test:** Tests a single small component (like a function) in isolation from others.  
  *Use when:* you want fast, repeatable checks during development.

- **Integration test:** Verifies that multiple modules work together properly.  
  *Use when:* checking that functions across files or systems interact correctly.

- **Regression test:** Ensures that previously fixed issues don’t reappear after new changes.  
  *Use when:* after a bug fix or feature addition, to lock in the correct behavior.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.

- **Pytest discovery:** Pytest automatically finds tests in files named `test_*.py` or `*_test.py`, and functions starting with `test_`.  
  No manual registration needed.

- **Fixture:** A reusable setup/cleanup function defined with `@pytest.fixture` that prepares data or environments for tests (e.g. `tmp_path` provides a temporary directory).

## Integration testing
- Created a test under `/tests/integration/test_order_integration.py` using the built-in `tmp_path` **fixture**.
- This test verifies interaction between `load_order`, `bulk_total`, and `write_receipt`.
- It uses temporary files (no manual cleanup) to simulate a real end-to-end workflow.

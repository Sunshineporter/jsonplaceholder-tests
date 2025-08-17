# JSONPlaceholder Service Unit Tests (pytest)

This repository contains a minimal, reproducible setup to perform **service unit tests** against the public JSONPlaceholder API.

## Structure
```
jsonplaceholder-tests/
├─ tests/
│  ├─ test_posts_api.py
│  ├─ test_contracts.py
│  ├─ test_errors_and_timeouts.py
│  ├─ test_idempotency.py
│  └─ conftest.py
├─ pytest.ini
├─ requirements.txt
└─ .github/workflows/tests.yml
```

## Quickstart
```bash
python -m venv venv
# Windows: venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt

# Run unit (stubbed/mocked) tests only (no internet required)
pytest -k "not integration"

# Run everything, including integration tests that hit the real API
pytest

# Coverage (optional, mainly useful when you wrap requests in your own client)
pytest --cov=. --cov-report=term-missing
```

## Notes
- Integration tests are marked with `@pytest.mark.integration`. Use the selector to include/exclude them in CI.
- For teaching/demo, JSONPlaceholder does **not** persist writes; this is expected.
- The repository demonstrates:

  - Contract testing (JSON Schema) for `/posts`
  - Positive and negative scenarios
  - Idempotency semantics checks (educational)
  - Stubbing timeouts and 404 responses with `responses`
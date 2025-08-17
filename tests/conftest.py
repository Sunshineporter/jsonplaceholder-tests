import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

BASE = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE
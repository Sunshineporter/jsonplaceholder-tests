from jsonschema import validate
import requests
import pytest

POST_SCHEMA = {
  "type": "object",
  "required": ["userId", "id", "title", "body"],
  "properties": {
    "userId": {"type": "integer"},
    "id":     {"type": "integer"},
    "title":  {"type": "string"},
    "body":   {"type": "string"}
  },
  "additionalProperties": True
}

@pytest.mark.integration
def test_get_posts_contract(base_url):
    r = requests.get(f"{base_url}/posts", timeout=10)
    assert r.status_code == 200
    assert r.headers.get("Content-Type","").startswith("application/json")
    data = r.json()
    assert isinstance(data, list) and len(data) > 0
    validate(instance=data[0], schema=POST_SCHEMA)
import pytest, requests

@pytest.mark.integration
def test_list_posts_ok(base_url):
    r = requests.get(f"{base_url}/posts", timeout=10)
    assert r.status_code == 200
    assert r.headers.get("Content-Type","").startswith("application/json")
    data = r.json()
    assert isinstance(data, list) and len(data) >= 100

@pytest.mark.integration
@pytest.mark.parametrize("pid", [1, 2, 3])
def test_get_post_detail_ok(base_url, pid):
    r = requests.get(f"{base_url}/posts/{pid}", timeout=10)
    assert r.status_code == 200
    j = r.json()
    assert j["id"] == pid and isinstance(j["title"], str)

@pytest.mark.integration
def test_create_post_ok(base_url):
    payload = {"title": "test", "body": "hello", "userId": 1}
    r = requests.post(f"{base_url}/posts", json=payload, timeout=10)
    assert r.status_code in (200, 201)
    j = r.json()
    for k in payload: 
        assert k in j
    assert "id" in j

@pytest.mark.integration
def test_update_post_put_ok(base_url):
    payload = {"id": 1, "title": "new", "body": "x", "userId": 1}
    r = requests.put(f"{base_url}/posts/1", json=payload, timeout=10)
    assert r.status_code == 200
    assert r.json()["title"] == "new"

@pytest.mark.integration
def test_delete_post_ok(base_url):
    r = requests.delete(f"{base_url}/posts/1", timeout=10)
    assert r.status_code in (200, 204)
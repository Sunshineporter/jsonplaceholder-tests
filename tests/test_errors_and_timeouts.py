import requests, responses

@responses.activate
def test_timeout_and_retry_stub(base_url):
    url = f"{base_url}/posts"
    responses.add(responses.GET, url, body=requests.Timeout())
    try:
        requests.get(url, timeout=0.001)  # intentionally tiny timeout
        assert False, "Should have raised Timeout"
    except requests.Timeout:
        pass

@responses.activate
def test_404_stub(base_url):
    url = f"{base_url}/non-exist"
    responses.add(responses.GET, url, json={"error": "not found"}, status=404)
    r = requests.get(url)
    assert r.status_code == 404
    assert r.json()["error"] == "not found"
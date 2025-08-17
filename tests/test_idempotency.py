import pytest, requests, responses, json

@pytest.mark.integration
def test_post_integration_returns_static_id_101(base_url):
    """JSONPlaceholder 是假 API，不持久化；POST /posts 总返回 id=101。
    这里断言“实际观测到的行为”，保证测试稳定。
    """
    payload = {"title": "t", "body": "b", "userId": 1}
    r1 = requests.post(f"{base_url}/posts", json=payload, timeout=10)
    r2 = requests.post(f"{base_url}/posts", json=payload, timeout=10)
    assert r1.status_code in (200, 201) and r2.status_code in (200, 201)
    assert r1.json().get("id") == 101 and r2.json().get("id") == 101

@responses.activate
def test_post_not_idempotent_semantics_stub(base_url):
    """纯单元（打桩）演示 POST 的“非幂等”语义：每次返回不同 id。"""
    url = f"{base_url}/posts"
    counter = {"n": 0}

    def responder(request):
        counter["n"] += 1
        new_id = 100 + counter["n"]
        body = json.loads(request.body or "{}")
        body["id"] = new_id
        return (201, {"Content-Type": "application/json"}, json.dumps(body))

    responses.add_callback(responses.POST, url, callback=responder,
                           content_type="application/json")
    payload = {"title": "t", "body": "b", "userId": 1}
    r1 = requests.post(url, json=payload)
    r2 = requests.post(url, json=payload)
    assert r1.json()["id"] != r2.json()["id"]

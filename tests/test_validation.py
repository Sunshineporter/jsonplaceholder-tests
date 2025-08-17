import pytest
import responses
from src.client import SimpleMath, JsonPlaceholderAPI

def test_sum_numbers_ok():
    assert SimpleMath.sum_numbers(2, 5) == 7

def test_sum_numbers_invalid_input():
    with pytest.raises(TypeError):
        SimpleMath.sum_numbers("x", 5)

@responses.activate
def test_get_post_validation_and_stub():
    client = JsonPlaceholderAPI

    # 非法输入
    with pytest.raises(ValueError):
        client.get_post(0)

    # mock 一个请求
    url = f"{client.BASE_URL}/posts/1"
    responses.add(responses.GET, url,
                  json={"id": 1, "title": "mock", "body": "test"},
                  status=200)

    data = client.get_post(1)
    assert data["id"] == 1
    assert data["title"] == "mock"

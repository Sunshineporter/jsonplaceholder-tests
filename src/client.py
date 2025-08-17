# src/client.py
import requests

class SimpleMath:
    """A trivial demo class for validation testing."""

    @staticmethod
    def sum_numbers(a, b):
        # 输入校验
        if not isinstance(a, (int, float)):
            raise TypeError("a must be int or float")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be int or float")
        return a + b


class JsonPlaceholderAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @classmethod
    def get_post(cls, post_id: int):
        if not isinstance(post_id, int) or post_id <= 0:
            raise ValueError("post_id must be a positive integer")
        r = requests.get(f"{cls.BASE_URL}/posts/{post_id}", timeout=5)
        r.raise_for_status()
        return r.json()

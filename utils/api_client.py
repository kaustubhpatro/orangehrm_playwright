import logging
import requests

log = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url: str):
        self.base = base_url.rstrip('/')

    def auth(self, user: str, pwd: str) -> str:
        response = requests.post(f"{self.base}/auth", json={"username": user, "password": pwd})
        response.raise_for_status()
        token = response.json().get("token")
        return token

    def create(self, data: dict) -> dict:
        response = requests.post(f"{self.base}/booking", json=data)
        response.raise_for_status()
        return response.json()

    def partial_update(self, booking_id: int, data: dict, token: str) -> dict:
        headers = {"Cookie": f"token={token}", "Content-Type": "application/json"}
        response = requests.patch(f"{self.base}/booking/{booking_id}", json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def get(self, booking_id: int) -> dict:
        response = requests.get(f"{self.base}/booking/{booking_id}")
        response.raise_for_status()
        return response.json()

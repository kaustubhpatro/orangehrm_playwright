import pytest
from utils.api_client import APIClient
import random
from datetime import date, timedelta
from faker import Faker

faker = Faker()
BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def client():
    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def token(client):
    return client.auth("admin", "password123")


def generate_booking_payload() -> dict:
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = random.randint(50, 500)
    depositpaid = random.choice([True, False])
    checkin = date.today().isoformat()
    checkout = (date.today() + timedelta(days=2)).isoformat()

    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        }
    }


@pytest.fixture
def booking_payload() -> dict:
    return generate_booking_payload()


@pytest.fixture
def booking(client, booking_payload):
    resp = client.create(booking_payload)
    return resp["bookingid"], booking_payload

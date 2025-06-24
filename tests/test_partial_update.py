from faker import Faker

faker = Faker()


def test_patch_booking(client, token, booking_payload, booking):
    bid = client.create(booking_payload)["bookingid"]
    new_lastname = faker.last_name()
    patch_payload = {"lastname": new_lastname}
    updated = client.partial_update(bid, patch_payload, token)
    assert updated["lastname"] == new_lastname
    booking = client.get(bid)
    assert booking["firstname"] == booking_payload["firstname"]
    assert booking["totalprice"] == booking_payload["totalprice"]
    assert booking["depositpaid"] == booking_payload["depositpaid"]
    assert booking["bookingdates"]["checkin"] == booking_payload["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == booking_payload["bookingdates"]["checkout"]

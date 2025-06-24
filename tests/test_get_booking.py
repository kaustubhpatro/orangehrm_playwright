def test_get_booking(client, booking_payload, booking):
    bid = client.create(booking_payload)["bookingid"]
    booking = client.get(bid)
    assert booking["firstname"] == booking_payload["firstname"]
    assert booking["lastname"] == booking_payload["lastname"]
    assert booking["totalprice"] == booking_payload["totalprice"]
    assert booking["depositpaid"] == booking_payload["depositpaid"]
    bd = booking["bookingdates"]
    assert bd["checkin"] == booking_payload["bookingdates"]["checkin"]
    assert bd["checkout"] == booking_payload["bookingdates"]["checkout"]
    expected = {"firstname", "lastname", "totalprice", "depositpaid", "bookingdates"}
    assert set(booking.keys()) == expected
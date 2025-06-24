def test_create_booking_success(client, booking_payload, booking):
    resp = client.create(booking_payload)
    assert "bookingid" in resp and isinstance(resp["bookingid"], int) and resp["bookingid"] > 0
    booking = resp["booking"]
    for key, val in booking_payload.items():
        assert booking[key] == val, f"{key!r} mismatch: {booking[key]} vs {val}"
    expected_keys = set(booking_payload.keys())
    assert set(booking.keys()) == expected_keys

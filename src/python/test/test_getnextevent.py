def test_next_event_return(client):
    response = client.get("/api/getnextevent")

    nextEvent = response.get_json()

    assert response.status_code == 200

    assert isinstance(nextEvent["eventRoundNumber"], int)
    assert isinstance(nextEvent["eventName"], str)
    assert isinstance(nextEvent["eventType"], str)
    assert isinstance(nextEvent["eventTime"], str)

def test_next_event_wrong_method(client):
    response = client.post("/api/getnextevent")

    assert response.status_code == 405
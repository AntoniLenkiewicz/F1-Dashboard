def test_schedule_return(client):
    response = client.get("/api/getschedule")

    schedule = response.get_json()

    assert response.status_code == 200
    for event in schedule:
        assert isinstance(event["eventName"], str)
        assert isinstance(event["eventStartDate"], str)
        assert isinstance(event["eventEndDate"], str)

def test_schedule_wrong_method(client):
    response = client.post("/api/getschedule")

    assert response.status_code == 405
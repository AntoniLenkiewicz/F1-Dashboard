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


def test_future_schedule(client):
    response = client.get("/api/getschedule?year=9999")

    assert response.status_code == 404


def test_schedule_wrong_data(client):
    response = client.get("/api/getschedule?year=year")

    assert response.status_code == 400

def test_schedule_negative_year(client):
    response = client.get("/api/getschedule?year=-5")
    assert response.status_code == 400

def test_schedule_pref1_year(client):
    response = client.get("/api/getschedule?year=1934")
    assert response.status_code == 400
    
def test_schedule_content_type(client):
    response = client.get("/api/getschedule")
    assert response.content_type == "application/json"
def test_current_driver_standings_return(client):
    driversStandings = client.get("/api/driverstandings")
    
    drivers = driversStandings.get_json()

    assert driversStandings.status_code == 200
    assert len(drivers) > 0
    for name, points in drivers.items():
        assert isinstance(name, str)
        assert isinstance(points, float)

def test_future_driver_standings(client):
    response = client.get("/api/driverstandings?year=9999")

    assert response.status_code == 404

def test_driver_standings_wrong_method(client):
    response = client.post("/api/driverstandings")

    assert response.status_code == 405

def test_driver_standings_wrong_data(client):
    response = client.get("/api/driverstandings?year=year")

    assert response.status_code == 400

def test_driver_standings_negative_year(client):
    response = client.get("/api/driverstandings?year=-5")
    assert response.status_code == 400

def test_driver_standings_pref1_year(client):
    response = client.get("/api/driverstandings?year=1934")
    assert response.status_code == 400
    
def test_driver_standings_content_type(client):
    response = client.get("/api/driverstandings")
    assert response.content_type == "application/json"
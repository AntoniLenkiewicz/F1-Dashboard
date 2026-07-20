def test_season_return(client):
    response = client.get("/api/getseasoninfo?year=2026")

    seasonInfo = response.get_json()

    assert response.status_code == 200
    assert isinstance(seasonInfo['year'], int)
    assert isinstance(seasonInfo['rounds'], int)

def test_season_wrong_method(client):
    response = client.post("/api/getseasoninfo")

    assert response.status_code == 405


def test_future_season(client):
    response = client.get("/api/getseasoninfo?year=9999")

    assert response.status_code == 404

def test_season_wrong_method(client):
    response = client.post("/api/getseasoninfo")

    assert response.status_code == 405

def test_season_wrong_data(client):
    response = client.get("/api/getseasoninfo?year=year")

    assert response.status_code == 400

def test_season_negative_year(client):
    response = client.get("/api/getseasoninfo?year=-5")
    assert response.status_code == 400

def test_season_pref1_year(client):
    response = client.get("/api/getseasoninfo?year=1934")
    assert response.status_code == 400
    
def test_season_content_type(client):
    response = client.get("/api/getseasoninfo")
    assert response.content_type == "application/json"
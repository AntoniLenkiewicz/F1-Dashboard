# GP is matched using fuzzy matching


def test_gpinfo_return(client):
    response = client.get("/api/getgpinfo?year=2026&gp=british%20grand%20prix")

    gpInfo = response.get_json()

    assert response.status_code == 200
    assert isinstance(gpInfo["eventRoundNumber"], int)
    assert isinstance(gpInfo["eventName"], str)
    assert isinstance(gpInfo["eventStartDate"], str)
    assert isinstance(gpInfo["eventEndDate"], str)

def test_gpinfo_return_nogp(client):
    response = client.get("/api/getgpinfo?year=2026")

    gpInfo = response.get_json()

    assert response.status_code == 200
    assert isinstance(gpInfo["eventRoundNumber"], int)
    assert isinstance(gpInfo["eventName"], str)
    assert isinstance(gpInfo["eventStartDate"], str)
    assert isinstance(gpInfo["eventEndDate"], str)

def test_gpinfo_wrong_method(client):
    response = client.post("/api/getgpinfo")

    assert response.status_code == 405


def test_future_gpinfo(client):
    response = client.get("/api/getgpinfo?year=9999&gp=british%20grand%20prix")

    assert response.status_code == 404


def test_gpinfo_wrong_data(client):
    response = client.get("/api/getgpinfo?year=year&gp=british%20grand%20prix")

    assert response.status_code == 400

def test_gpinfo_negative_year(client):
    response = client.get("/api/getgpinfo?year=-5&gp=british%20grand%20prix")
    assert response.status_code == 400

def test_gpinfo_pref1_year(client):
    response = client.get("/api/getgpinfo?year=1934&gp=british%20grand%20prix")
    assert response.status_code == 400
    
def test_gpinfo_content_type(client):
    response = client.get("/api/getgpinfo")
    assert response.content_type == "application/json"
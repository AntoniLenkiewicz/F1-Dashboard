def test_current_team_standings_return(client):
    teamStandings = client.get("/api/teamstandings")
    
    teams = teamStandings.get_json()

    assert teamStandings.status_code == 200
    assert len(teams) > 0
    for name, points in teams.items():
        assert isinstance(name, str)
        assert isinstance(points, float)

def test_future_team_standings(client):
    response = client.get("/api/teamstandings?year=9999")

    assert response.status_code == 404

def test_team_standings_wrong_method(client):
    response = client.post("/api/teamstandings")

    assert response.status_code == 405

def test_team_standings_wrong_data(client):
    response = client.get("/api/teamstandings?year=year")

    assert response.status_code == 400

def test_team_standings_negative_year(client):
    response = client.get("/api/teamstandings?year=-5")
    assert response.status_code == 400

def test_team_standings_pref1_year(client):
    response = client.get("/api/teamstandings?year=1934")
    assert response.status_code == 400
    
def test_team_standings_content_type(client):
    response = client.get("/api/teamstandings")
    assert response.content_type == "application/json"
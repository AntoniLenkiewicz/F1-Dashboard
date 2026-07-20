# GP is matched using fuzzy matching
def test_gpresults_return_nogp_noyear_nosession(client):
    response = client.get("/api/getgpresults")

    gpResults = response.get_json()

    columns = gpResults['columns']
    sessions = gpResults['allSessions']
    results = gpResults['results']

    assert response.status_code == 200
    assert isinstance(gpResults['sessionName'], str)
    
    for col in columns:
        assert isinstance(col, str)
    
    for session in sessions:
        assert isinstance(session, str)
    
    if gpResults['sessionName'] == 'Race' or gpResults == 'Sprint Race':
        for result in results:
            assert isinstance(result['pos'], int)
            assert isinstance(result['num'], int)
            assert isinstance(result['lastName'], str)
            assert isinstance(result['team'], str)
            assert isinstance(result['time'], str)
            assert isinstance(result['laps'], int)
            assert isinstance(result['points'], float)

    elif 'Practice' in gpResults['sessionName']:
        for result in results:
            assert isinstance(result['num'], int)
            assert isinstance(result['lastName'], str)
            assert isinstance(result['team'], str)
            assert isinstance(result['bestTime'], str)
            assert isinstance(result['laps'], int)

    elif 'Qualifying' in gpResults['sessionName']:
        for result in results:
            assert isinstance(result['pos'], int)
            assert isinstance(result['num'], int)
            assert isinstance(result['lastName'], str)
            assert isinstance(result['team'], str)
            assert isinstance(result['q1'], str)
            assert isinstance(result['q2'], str)
            assert isinstance(result['q3'], str)

def test_gpresults_return_race(client):
    response = client.get("/api/getgpresults?year=2026&gp=british%20grand%20prix&session=race")

    gpResults = response.get_json()

    columns = gpResults['columns']
    sessions = gpResults['allSessions']
    results = gpResults['results']

    assert response.status_code == 200
    assert isinstance(gpResults['sessionName'], str)
    
    for col in columns:
        assert isinstance(col, str)
    
    for session in sessions:
        assert isinstance(session, str)
    
    if gpResults['sessionName'] == 'Race' or gpResults == 'Sprint Race':
        for result in results:
            assert isinstance(result['pos'], int)
            assert isinstance(result['num'], int)
            assert isinstance(result['lastName'], str)
            assert isinstance(result['team'], str)
            assert isinstance(result['time'], str)
            assert isinstance(result['laps'], int)
            assert isinstance(result['points'], float)

    elif 'Practice' in gpResults['sessionName']:
        for result in results:
            assert isinstance(result['num'], int)
            assert isinstance(result['lastName'], str)
            assert isinstance(result['team'], str)
            assert isinstance(result['bestTime'], str)
            assert isinstance(result['laps'], int)

    elif 'Qualifying' in gpResults['sessionName']:
        for result in results:
            assert isinstance(result['pos'], int)
            assert isinstance(result['num'], int)
            assert isinstance(result['lastName'], str)
            assert isinstance(result['team'], str)
            assert isinstance(result['q1'], str)
            assert isinstance(result['q2'], str)
            assert isinstance(result['q3'], str)


def test_gpresults_return_pracitce(client):
    response = client.get("/api/getgpresults?year=2026&gp=british%20grand%20prix&session=practice%201")

    gpResults = response.get_json()

    columns = gpResults['columns']
    sessions = gpResults['allSessions']
    results = gpResults['results']

    assert response.status_code == 200
    assert isinstance(gpResults['sessionName'], str)
    
    for col in columns:
        assert isinstance(col, str)
    
    for session in sessions:
        assert isinstance(session, str)

    assert gpResults['sessionName'] == 'Practice 1'

    for result in results:
        assert isinstance(result['num'], int)
        assert isinstance(result['lastName'], str)
        assert isinstance(result['team'], str)
        assert isinstance(result['bestTime'], str)
        assert isinstance(result['laps'], int)


def test_gpresults_return_quali(client):
    response = client.get("/api/getgpresults?year=2026&gp=british%20grand%20prix&session=qualifying")

    gpResults = response.get_json()

    columns = gpResults['columns']
    sessions = gpResults['allSessions']
    results = gpResults['results']

    assert response.status_code == 200
    assert isinstance(gpResults['sessionName'], str)
    
    for col in columns:
        assert isinstance(col, str)
    
    for session in sessions:
        assert isinstance(session, str)
    
    assert gpResults['sessionName'] == 'Qualifying'
    for result in results:
        assert isinstance(result['pos'], int)
        assert isinstance(result['num'], int)
        assert isinstance(result['lastName'], str)
        assert isinstance(result['team'], str)
        assert isinstance(result['q1'], str)
        assert isinstance(result['q2'], str)
        assert isinstance(result['q3'], str)

def test_gpresultswrong_method(client):
    response = client.post("/api/getgpresults")

    assert response.status_code == 405


def test_future_gpresults(client):
    response = client.get("/api/getgpresults?year=9999&gp=british%20grand%20prix")

    assert response.status_code == 404


def test_gpresultswrong_data(client):
    response = client.get("/api/getgpresults?year=year&gp=british%20grand%20prix")

    assert response.status_code == 400

def test_gpresultsnegative_year(client):
    response = client.get("/api/getgpresults?year=-5&gp=british%20grand%20prix")
    assert response.status_code == 400

def test_gpresultspref1_year(client):
    response = client.get("/api/getgpresults?year=1934&gp=british%20grand%20prix")
    assert response.status_code == 400
    
def test_gpresultscontent_type(client):
    response = client.get("/api/getgpresults")
    assert response.content_type == "application/json"
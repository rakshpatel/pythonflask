import requests

HOST="http://localhost:5000"

def test_get_all_ships_success():
    response = requests.get("{}/api/ships".format(HOST))
    assert response.status_code == 200
    

def test_get_all_ships_nodata():
    response = requests.get("{}/api/ships".format(HOST))
    response = response.json()
    assert not response["ship"] == "No data found"

def test_get_position_success():
    imo = 1
    response = requests.get("{}/api/positions/{}".format(HOST, imo))
    response = response.json()
    assert response["ship"] == "no data found for imo: {}".format(imo)
    
def test_get_position_nodata():
    imo = 9632179
    response = requests.get("{}/api/positions/{}".format(HOST, imo))
    response = response.json()
    assert not response["ship"] == "no data found for imo: {}".format(imo)
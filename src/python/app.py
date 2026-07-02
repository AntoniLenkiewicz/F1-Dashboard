import time
from datetime import datetime, timezone
from flask import Flask, jsonify, request
import fastf1
from models import GetDriverStandings, GetTeamStandings

fastf1.Cache.enable_cache("./cache")

session = fastf1.get_session(2026, "Austria", "Race")
session.load()
messages = session.race_control_messages
lapData = session.laps
laps = lapData.pick_drivers('VER')
telemetry = laps.get_car_data()
position = laps.get_pos_data()


app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/driverstandings')
def get_driver_standings():
    year = datetime.now().year
    season = int(request.args.get('year', year))
    driver_standings = GetDriverStandings(season)
    print(driver_standings)
    return(driver_standings)

@app.route('/api/teamstandings')
def get_team_standings():
    year = datetime.now().year
    season = int(request.args.get('year', year))
    team_standings = GetTeamStandings(season)
    print(team_standings)
    return(team_standings)

# fast f1 
def on_message(msg):
    print(msg)


def main():
    from fastf1.livetiming.client import SignalRClient

    client = SignalRClient(
        filename="dump.txt",
        filemode="w",
        debug=False,
        timeout=0,
        no_auth=False
    )

    # override internal handler so we just print data
    client._on_message = lambda msg: on_message(msg)

    print("Connecting to F1 live timing...")

    client.start()
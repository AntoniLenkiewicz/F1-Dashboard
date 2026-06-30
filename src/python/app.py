import time
from flask import Flask
import fastf1

fastf1.Cache.enable_cache("./cache")

session = fastf1.get_session(2026, "Austria", "Race")
session.load()
messages = session.race_control_messages
lapData = session.laps
laps = lapData.pick_drivers('VER')
telemetry = laps.get_car_data()
position = laps.get_pos_data()
print(telemetry.head())
print(position.head())


app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}




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
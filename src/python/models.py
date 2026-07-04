import flask
import fastf1
from datetime import datetime, timezone
from flask import Flask
from fastf1.livetiming.client import SignalRClient
import math

def GetDriverStandings(season):
    schedule = fastf1.get_event_schedule(season, include_testing=False)
    standings = {}
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        eventName, sprintStart, raceStart, eventFormat = event["EventName"], event["Session3DateUtc"], event["Session5DateUtc"], event["EventFormat"]

        if eventFormat == "sprint_qualifying" and str(sprintStart) < str(currentDate):
            sprint = fastf1.get_session(season, eventName, "S")
            sprint.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverSprintData in sprint.results.iterrows():
                if driverSprintData["Abbreviation"] not in standings:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings[driverSprintData["Abbreviation"]] = driverSprintData["Points"]
                else:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings[driverSprintData["Abbreviation"]] = standings[driverSprintData["Abbreviation"]] + driverSprintData["Points"]

        if str(raceStart) < str(currentDate):
            race = fastf1.get_session(season, eventName, "R")
            race.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverRaceData in race.results.iterrows():
                if driverRaceData["Abbreviation"] not in standings:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings[driverRaceData["Abbreviation"]] = driverRaceData["Points"]
                else:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings[driverRaceData["Abbreviation"]] = standings[driverRaceData["Abbreviation"]] + driverRaceData["Points"]
    return (standings)


def GetTeamStandings(season):
    schedule = fastf1.get_event_schedule(season, include_testing=False)
    standings = {}
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        eventName, sprintStart, raceStart, eventFormat = event["EventName"], event["Session3DateUtc"], event["Session5DateUtc"], event["EventFormat"]

        if eventFormat == "sprint_qualifying" and str(sprintStart) < str(currentDate):
            sprint = fastf1.get_session(season, eventName, "S")
            sprint.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverSprintData in sprint.results.iterrows():
                if driverSprintData["TeamName"] not in standings:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings[driverSprintData["TeamName"]] = driverSprintData["Points"]
                else:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings[driverSprintData["TeamName"]] = standings[driverSprintData["TeamName"]] + driverSprintData["Points"]

        if str(raceStart) < str(currentDate):
            race = fastf1.get_session(season, eventName, "R")
            race.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverRaceData in race.results.iterrows():
                if driverRaceData["TeamName"] not in standings:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings[driverRaceData["TeamName"]] = driverRaceData["Points"]
                else:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings[driverRaceData["TeamName"]] = standings[driverRaceData["TeamName"]] + driverRaceData["Points"]
    return (standings)

# Will need updating later to return whether the event is currently underway
def GetNextEvent():
    year = datetime.now().year
    schedule = fastf1.get_event_schedule(year, include_testing=False)
    currentDate = datetime.now(timezone.utc)
    next_event = ''
    for _, event in schedule.iterrows():
        for i in range(1,6):
            if str(event[f"Session{i}DateUtc"]) > str(currentDate):
                print(event)
                return {"eventName": event["EventName"],"eventType" : event[(f"Session{i}")], "eventRoundNumber" : event["RoundNumber"] }

GetNextEvent()
# Trial for getting live data

# from fastf1.livetiming.client import SignalRClient

# client = SignalRClient(
#     filename='session_data.txt',
#     filemode='w',
#     debug=False,
#     timeout=60,
#     logger=None,
#     no_auth=False
# )

# client.start()
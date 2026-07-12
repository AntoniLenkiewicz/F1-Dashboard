import flask
import fastf1
from datetime import datetime, timezone
from flask import Flask, jsonify
from fastf1.livetiming.client import SignalRClient
from fastf1.ergast import Ergast
import math
import time
import numpy as np

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
                return {"eventName": event["EventName"],
                        "eventType" : event[(f"Session{i}")], 
                        "eventRoundNumber" : event["RoundNumber"], 
                        "eventTime": str(event[(f"Session{i}DateUtc")])}
def GetSchedule():
    year = datetime.now().year
    events = []
    schedule = fastf1.get_event_schedule(year, include_testing=False)
    for _, event in schedule.iterrows():
        events.append({"eventName" : event["EventName"], "eventStart" : str(event["Session1DateUtc"])[:10], "eventEnd" : str(event["Session5DateUtc"])[:10]})
    return events


def GetGrandPrixInfo(year, grandPrix):
    event = fastf1.get_event(year, grandPrix)
    return {"eventName": event["EventName"], "eventRoundNumber" : int(event["RoundNumber"]), "eventStart" : str(event["Session1DateUtc"])[:10], "eventEnd" : str(event["Session5DateUtc"])[:10]}


def GetGrandPrixResults(year, grandPrix, *args, **kwargs):
    selectedSession = kwargs.get('session', 0)
    event = fastf1.get_event(year, grandPrix)
    sessionDates = [event.Session1DateUtc, event.Session2DateUtc, event.Session3DateUtc, event.Session4DateUtc, event.Session5DateUtc]
    sessionNames = [event.Session1, event.Session2, event.Session3, event.Session4, event.Session5]
    if not selectedSession:
        sessionNum = 0
        date = datetime.now()
        for i in sessionDates:
            if date > i:
                sessionNum = sessionNum + 1
        session = fastf1.get_session(year, grandPrix, sessionNum)
    else:
        session = fastf1.get_session(year, grandPrix, selectedSession)
    session.load()
    session.results[['Time', 'Q1', 'Q2', 'Q3']] = session.results[['Time', 'Q1', 'Q2', 'Q3']].astype(str)
    session.results.rename(columns={"Position":"Pos", "DriverNumber" : "Num", "TeamName": "Team"}, inplace=True)
    columns = []
    if session.name == 'Race' or session.name == 'Sprint':
        columns = ['Pos','Num', 'LastName', 'Team', 'Time', 'Laps', 'Points']
    elif 'Practice' in session.name:
        print("practice")
    elif 'Qualifying' in session.name:
        columns = ['Pos', 'Num','LastName', 'Team', 'Q1', 'Q2', 'Q3']
    results = session.results[columns]
    results = results.replace({np.nan:None}).to_dict(orient="records")
    return {"sessionName":session.name, "allSessionNames": sessionNames, "sessionResults": results, "columns":columns}

# print(GetGrandPrixResults(2025, "British GP", session=1)['sessionResults']['Time'])
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
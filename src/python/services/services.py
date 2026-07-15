import sys
import fastf1
from datetime import datetime, timezone
import math
import numpy as np
from dataclasses import asdict, dataclass

sys.path.insert(1, 'models')
from models import NextEvent, EventDetails, Schedule, DriverPoints, TeamPoints, DriverQualiResults, DriverRaceResults, DriverPracticeResults, GPResults

def GetDriverStandings(season):
    schedule = fastf1.get_event_schedule(season, include_testing=False)
    standings = DriverPoints(points={})
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        eventName, sprintStart, raceStart, eventFormat = event["EventName"], event["Session3DateUtc"], event["Session5DateUtc"], event["EventFormat"]

        if eventFormat == "sprint_qualifying" and str(sprintStart) < str(currentDate):
            sprint = fastf1.get_session(season, eventName, "S")
            sprint.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverSprintData in sprint.results.iterrows():
                if driverSprintData["Abbreviation"] not in standings.points:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings.points[driverSprintData["Abbreviation"]] = driverSprintData["Points"]
                else:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings.points[driverSprintData["Abbreviation"]] = standings.points[driverSprintData["Abbreviation"]] + driverSprintData["Points"]

        if str(raceStart) < str(currentDate):
            race = fastf1.get_session(season, eventName, "R")
            race.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverRaceData in race.results.iterrows():
                if driverRaceData["Abbreviation"] not in standings.points:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings.points[driverRaceData["Abbreviation"]] = driverRaceData["Points"]
                else:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings.points[driverRaceData["Abbreviation"]] = standings.points[driverRaceData["Abbreviation"]] + driverRaceData["Points"]
    return (standings.points)



def GetTeamStandings(season):
    schedule = fastf1.get_event_schedule(season, include_testing=False)
    standings = TeamPoints(points = {})
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        eventName, sprintStart, raceStart, eventFormat = event["EventName"], event["Session3DateUtc"], event["Session5DateUtc"], event["EventFormat"]

        if eventFormat == "sprint_qualifying" and str(sprintStart) < str(currentDate):
            sprint = fastf1.get_session(season, eventName, "S")
            sprint.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverSprintData in sprint.results.iterrows():
                if driverSprintData["TeamName"] not in standings.points:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings.points[driverSprintData["TeamName"]] = driverSprintData["Points"]
                else:
                    if math.isnan(driverSprintData["Points"]):
                        driverSprintData["Points"] = 0
                    standings.points[driverSprintData["TeamName"]] = standings.points[driverSprintData["TeamName"]] + driverSprintData["Points"]

        if str(raceStart) < str(currentDate):
            race = fastf1.get_session(season, eventName, "R")
            race.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, driverRaceData in race.results.iterrows():
                if driverRaceData["TeamName"] not in standings.points:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings.points[driverRaceData["TeamName"]] = driverRaceData["Points"]
                else:
                    if math.isnan(driverRaceData["Points"]):
                        driverRaceData["Points"] = 0
                    standings.points[driverRaceData["TeamName"]] = standings.points[driverRaceData["TeamName"]] + driverRaceData["Points"]
    return (standings.points)

# Will need updating later to return whether the event is currently underway
def GetNextEvent():
    year = datetime.now().year
    schedule = fastf1.get_event_schedule(year, include_testing=False)
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        for i in range(1,6):
            if str(event[f"Session{i}DateUtc"]) > str(currentDate):
                nextEvent = NextEvent(
                    roundNumber = event["RoundNumber"],
                    eventName = event["EventName"],
                    eventType = str(event[(f"Session{i}")]),
                    eventTime = str(event[(f"Session{i}DateUtc")])
                )
                return asdict(nextEvent)
def GetSchedule():
    year = datetime.now().year
    scheduledEvents = Schedule(events=[])
    schedule = fastf1.get_event_schedule(year, include_testing=False)
    for _, event in schedule.iterrows():
        scheduledEvent = EventDetails(
            eventRoundNumber = event["RoundNumber"],
            eventName = event["EventName"],
            eventStartDate = str(event["Session1DateUtc"])[:10],
            eventEndDate = str(event["Session5DateUtc"])[:10]
        )
        scheduledEvents.events.append(scheduledEvent)
    print(scheduledEvents.events)
    return (scheduledEvents.events)


def GetGrandPrixInfo(year, grandPrix):
    event = fastf1.get_event(year, grandPrix)
    eventDetails = EventDetails(
            eventRoundNumber = int(event["RoundNumber"]),
            eventName = event["EventName"],
            eventStartDate = str(event["Session1DateUtc"])[:10],
            eventEndDate = str(event["Session5DateUtc"])[:10]
        )
    print(asdict(eventDetails))
    return asdict(eventDetails)

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
    session.load(laps=True)
    session.results[['Time', 'Q1', 'Q2', 'Q3']] = session.results[['Time', 'Q1', 'Q2', 'Q3']].astype(str)
    session.results.rename(columns={"Position":"Pos", "DriverNumber" : "Num", "TeamName": "Team"}, inplace=True)
    # circuit_info = session.get_circuit_info()

    if session.name == 'Race' or session.name == 'Sprint':
        results = GPResults(
            sessionName = str(session.name),
            results = [],
            allSessions = sessionNames,
            columns = ['pos', 'num', 'lastName', 'team', 'time', 'laps', 'points']
        )
        for _, driverResult in session.results.iterrows():
            driverRaceResult = DriverRaceResults(
                pos = int(driverResult['Pos']),
                num = int(driverResult['Num']),
                lastName = str(driverResult['LastName']),
                team = str(driverResult['Team']),
                time = str(driverResult['Time']),
                laps = int(driverResult['Laps']),
                points = float(driverResult['Points'])
            )
            results.results.append(driverRaceResult)

    elif 'Practice' in session.name:
        results = GPResults(
            sessionName = str(session.name),
            results = [],
            allSessions = sessionNames,
            columns = ['pos', 'num', 'lastName', 'team', 'bestTime', 'laps']
        )
        laps = session.laps
        filteredSession = session.results.replace({np.nan:0})
        for _, driverResult in filteredSession.iterrows():
            driver = driverResult['Abbreviation']
            totalLaps=len(laps.pick_drivers(driver))
            fastestLap = laps.pick_drivers(driver).pick_fastest()
            driverPracticeResult = DriverPracticeResults(
                pos = int(driverResult['Pos']),
                num = int(driverResult['Num']),
                lastName = str(driverResult['LastName']),
                team = str(driverResult['Team']),
                bestTime = str(fastestLap.LapTime),
                laps = int(totalLaps)
            )
            results.results.append(driverPracticeResult)

    elif 'Qualifying' in session.name:
        results = GPResults(
            sessionName = str(session.name),
            results = [],
            allSessions = sessionNames,
            columns = ['pos', 'num', 'lastName', 'team', 'q1', 'q2', 'q3']
        )
        for _, driverResult in session.results.iterrows():
            driverQualiResult = DriverQualiResults(
                pos = int(driverResult['Pos']),
                num = int(driverResult['Num']),
                lastName = str(driverResult['LastName']),
                team = str(driverResult['Team']),
                q1 = str(driverResult['Q1']),
                q2 = str(driverResult['Q2']),
                q3 = str(driverResult['Q3'])
            )
            results.results.append(driverQualiResult)
    return asdict(results)

print(GetGrandPrixResults(2026, "British", session = 5))
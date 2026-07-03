import flask
import fastf1
from datetime import datetime, timezone
from flask import Flask
from fastf1.livetiming.client import SignalRClient

def GetDriverStandings(season):
    schedule = fastf1.get_event_schedule(season, include_testing=False)
    standings = {}
    short_event_names = []
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        event_name, round_number, sprint_start, race_start = event["EventName"], event["RoundNumber"], event["Session3DateUtc"], event["Session5DateUtc"]
        short_event_names.append(event_name.replace("Grand Prix", "").strip())
        if str(sprint_start) > str(currentDate):
            break

        # Load race results
        if str(race_start) < str(currentDate):
            race = fastf1.get_session(season, event_name, "R")
            race.load(laps=False, telemetry=False, weather=False, messages=False)
        
        # Check for sprint race
        sprint = None
        if event["EventFormat"] == "sprint_qualifying":
            sprint = fastf1.get_session(season, event_name, "S")
            sprint.load(laps=False, telemetry=False, weather=False, messages=False)
        for _, driver_row in race.results.iterrows():
            abbreviation, race_points, race_position = (
                driver_row["Abbreviation"],
                driver_row["Points"],
                driver_row["Position"]
            )
            
            sprint_points = 0
            if sprint is not None:
                driver_row = sprint.results[
                    sprint.results["Abbreviation"] == abbreviation
                ]
                if not driver_row.empty:
                    sprint_points = driver_row["Points"].values[0]
            

            if abbreviation not in standings:
                standings[abbreviation]=int(race_points + sprint_points)
            
            else:
                standings[abbreviation] = standings[abbreviation] + int((race_points + sprint_points))
    return standings

def GetTeamStandings(season):
    schedule = fastf1.get_event_schedule(season, include_testing=False)
    standings = {}
    short_event_names = []
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        event_name, round_number, sprint_start, race_start = event["EventName"], event["RoundNumber"], event["Session3DateUtc"], event["Session5DateUtc"]
        short_event_names.append(event_name.replace("Grand Prix", "").strip())
        if str(sprint_start) > str(currentDate):
            break

        # Load race results
        if str(race_start) < str(currentDate):
            race = fastf1.get_session(season, event_name, "R")
            race.load(laps=False, telemetry=False, weather=False, messages=False)
        
        # Check for sprint race
        sprint = None
        if event["EventFormat"] == "sprint_qualifying":
            sprint = fastf1.get_session(season, event_name, "S")
            sprint.load(laps=False, telemetry=False, weather=False, messages=False)
        for _, driver_row in race.results.iterrows():
            abbreviation, race_points, race_position, teamName = (
                driver_row["Abbreviation"],
                driver_row["Points"],
                driver_row["Position"],
                driver_row["TeamName"]
            )
            
            sprint_points = 0
            if sprint is not None:
                driver_row = sprint.results[
                    sprint.results["TeamName"] == teamName
                ]
                if not driver_row.empty:
                    sprint_points = driver_row["Points"].values[0]
            

            if teamName not in standings:
                standings[teamName]=int(race_points + sprint_points)
            
            else:
                standings[teamName] = standings[teamName] + int((race_points + sprint_points))
    return standings

# Will need updating later to return whether the event is currently underway
def GetNextEvent():
    year = datetime.now().year
    schedule = fastf1.get_event_schedule(year, include_testing=False)
    currentDate = datetime.now(timezone.utc)
    next_event = ''
    for _, event in schedule.iterrows():
        for i in range(1,6):
            if str(event[f"Session{i}DateUtc"]) > str(currentDate):
                return {"eventName": event["EventName"],"eventType" : event["EventFormat"], "eventRoundNumber" : event["RoundNumber"] }


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
import flask
import fastf1
from datetime import datetime, timezone
from flask import Flask


def GetDriverStandings(season):
    schedule = fastf1.get_event_schedule(season, include_testing=False)
    standings = {}
    short_event_names = []
    currentDate = datetime.now(timezone.utc)
    for _, event in schedule.iterrows():
        event_name, round_number, event_start = event["EventName"], event["RoundNumber"], event["Session1DateUtc"]
        short_event_names.append(event_name.replace("Grand Prix", "").strip())
        if str(event_start) > str(currentDate):
            break

        # Load race results
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
        event_name, round_number, event_start = event["EventName"], event["RoundNumber"], event["Session1DateUtc"]
        short_event_names.append(event_name.replace("Grand Prix", "").strip())
        if str(event_start) > str(currentDate):
            break

        # Load race results
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
print(GetTeamStandings(2026))
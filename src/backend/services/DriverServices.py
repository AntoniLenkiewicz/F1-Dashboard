import sys
import fastf1
from datetime import datetime, timezone
import math
import numpy as np
from dataclasses import asdict, dataclass

sys.path.insert(1, 'models')
from DriverModels import DriverPoints


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
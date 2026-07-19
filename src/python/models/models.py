from dataclasses import dataclass

@dataclass
class NextEvent:
    roundNumber: int
    eventName: str
    eventType: str
    eventTime: str

@dataclass
class EventDetails:
    eventRoundNumber: int
    eventName: str
    eventStartDate: str
    eventEndDate: str

@dataclass
class Schedule:
    events: list[EventDetails]

@dataclass
class DriverPoints:
    points: dict[str, float]

@dataclass
class TeamPoints:
    points: dict[str, float]

@dataclass
class GPResults:
    sessionName: str
    results: list[DriverRaceResults] | list[DriverQualiResults] | list[DriverPracticeResults]
    allSessions: list[str]
    columns: list[str]

@dataclass
class DriverRaceResults:
    pos: int
    num: int
    lastName: str
    team: str
    time: str #unless I find a better datatype
    laps: int 
    points: float

@dataclass
class DriverQualiResults:
    pos: int
    num: int
    lastName: str
    team: str
    q1: str #unless I find a better datatype
    q2: str #unless I find a better datatype
    q3: str #unless I find a better datatype

@dataclass
class DriverPracticeResults:
    num: int
    lastName: str
    team: str
    bestTime: str
    laps: int

@dataclass
class SeasonInformation:
    year: int
    rounds: int
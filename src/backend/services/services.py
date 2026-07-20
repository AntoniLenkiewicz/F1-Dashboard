import sys
import fastf1
from datetime import datetime, timezone
import math
import numpy as np
from dataclasses import asdict, dataclass

sys.path.insert(1, 'models')
from models import NextEvent, EventDetails, Schedule, DriverPoints, TeamPoints, DriverQualiResults, DriverRaceResults, DriverPracticeResults, GPResults, SeasonInformation

import sys
import time
from datetime import datetime, timezone
from flask import Flask, jsonify, request
import fastf1

from TeamControllers import TeamControllers
from EventControllers import EventControllers
from DriverControllers import DriverControllers

def routes(app):
    @app.route('/api/time')
    def get_current_time():
        return {'time': time.time()}
    
    EventControllers(app)

    TeamControllers(app)

    DriverControllers(app)


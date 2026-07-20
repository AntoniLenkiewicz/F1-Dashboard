import sys
import time
from datetime import datetime, timezone
from flask import Flask, jsonify, request
import fastf1

sys.path.insert(1, 'services')
from DriverServices import GetDriverStandings

def DriverControllers(app):
    @app.route('/api/driverstandings')
    def get_driver_standings():
        try:
            year = datetime.now().year
            season = int(request.args.get('year', year))
            if season > year:
                return 'Content not found', 404
            elif season < 1950:
                return 'Bad Request', 400
            try:
                driver_standings = GetDriverStandings(season)
                return(driver_standings)
            except:
                return 'Server Error', 500
        except:
            return 'Bad Request', 400
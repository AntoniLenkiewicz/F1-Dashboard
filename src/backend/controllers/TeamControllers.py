import sys
import time
from datetime import datetime, timezone
from flask import Flask, jsonify, request
import fastf1

sys.path.insert(1, 'services')
from TeamServices import GetTeamStandings


def TeamControllers(app):

    @app.route('/api/teamstandings')
    def get_team_standings():
        try:
            year = datetime.now().year
            season = int(request.args.get('year', year))
            if season > year:
                return 'Content not found', 404
            elif season < 1950:
                return 'Bad Request', 400
            try:
                team_standings = GetTeamStandings(season)
                return(team_standings)
            except:
                return 'Server Error', 500
        except:
            return 'Bad Request', 400
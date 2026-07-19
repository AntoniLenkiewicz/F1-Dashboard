import sys
import time
from datetime import datetime, timezone
from flask import Flask, jsonify, request
import fastf1

sys.path.insert(1, 'services')
from services import GetDriverStandings, GetTeamStandings, GetNextEvent, GetSchedule, GetGrandPrixResults, GetGrandPrixInfo, GetSeasonInfo

def routes(app):
    @app.route('/api/time')
    def get_current_time():
        return {'time': time.time()}


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

    @app.route('/api/getnextevent')
    def get_next_event():
        event = GetNextEvent()
        return event

    @app.route('/api/getschedule')
    def get_event_schedule():
        try:
            year = datetime.now().year
            season = int(request.args.get('year', year))
            schedule = GetSchedule(season)
            return schedule
        except:
            return 'Bad Request', 400

    @app.route('/api/getgpresults')
    def get_gp_results():
        try:
            year = datetime.now().year
            season = int(request.args.get('year', year))
            grandPrixName = str(request.args.get('gp', ''))
            session = str(request.args.get('session', ''))
            if season > year:
                return 'Content not found', 404
            elif season < 1950:
                return 'Bad Request', 400
            try:
                results = GetGrandPrixResults(season, grandPrixName, session = session)
                return results
            except:
                return 'Server Error', 500
        except:
            return 'Bad Request', 400
        
    @app.route('/api/getgpinfo')
    def get_gp_info():
        try:
            year = datetime.now().year
            season = int(request.args.get('year', year))
            grandPrixName = str(request.args.get('gp', ''))
            if season > year:
                return 'Content not found', 404
            elif season < 1950:
                return 'Bad Request', 400
            try:
                gpInfo = GetGrandPrixInfo(season, grandPrixName)
                return gpInfo
            except:
                return 'Server Error', 500
        except:
            return 'Bad Request', 400
    
    @app.route('/api/getseasoninfo')
    def get_season_info():
        try:
            year = datetime.now().year
            season = int(request.args.get('year', year))
            if season > year:
                return 'Content not found', 404
            elif season < 1950:
                return 'Bad Request', 400
            try:
                seasonInfo = GetSeasonInfo(season)
                return seasonInfo
            except:
                return 'Server Error', 500
        except:
            return 'Bad Request', 400
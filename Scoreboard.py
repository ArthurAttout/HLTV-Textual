from __future__ import annotations
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Static, Placeholder

from ScoreboardTopHeader import ScoreboardTopHeader
from TeamStats import TeamStats
from Timeline import Timeline
from ScoreboardTopHeader import ScoreboardData
from TeamStats import PlayerStat
import socketio
import json

TEAM_STATS = [
    PlayerStat("deko",        False, "WP",100,True,1430,4,1,2,87.0),
    PlayerStat("Boombl4",     False,"AWP",100,True,1430,4,1,2,87.0),
    PlayerStat("TRAVIS",      True,"AWP",100,True,1430,4,1,2,87.0),
    PlayerStat("NickelBack",  False,"AWP",100,True,1430,4,1,2,87.0),
    PlayerStat("Forester",    True,"AWP",100,True,1430,4,1,2,87.0),
]

SCOREBOARD_DATA = ScoreboardData(13, "Overpass", "10", 4, 8)

class ScoreboardApp(App):
    counter = 0
    CSS_PATH = "Scoreboard.css"

    def __init__(self):
        App.__init__(self)

    def compose(self) -> ComposeResult:
        yield Header()
        yield ScoreboardTopHeader(SCOREBOARD_DATA)
        yield TeamStats(TEAM_STATS)
        yield Timeline()
        yield TeamStats(TEAM_STATS)
        yield Footer()


    def update_data(self, data:ScoreboardData):
        self.query_one(ScoreboardTopHeader).update_data(data)
        
if __name__ == "__main__":
    app = ScoreboardApp()
    
    sio = socketio.Client(reconnection_attempts=8)
    @sio.event
    def connect():
        print('connection established')

    @sio.event
    def scoreboard(data):
        round = data['currentRound']
        map_name = data['mapName']
        time = '0'
        ct_score = data['counterTerroristScore']
        t_score = data['terroristScore']
        new_data = ScoreboardData(round,map_name,time,ct_score,t_score)
        app.update_data(new_data)

    @sio.event
    def log(data):
        pass

    @sio.event
    def disconnect():
        print('disconnected from server')

    sio.connect('http://localhost:8080')
    app.run()


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
import threading 
# Declraing a lock
lock = threading.Lock()

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
        yield TeamStats(TEAM_STATS, id='stats_t')
        yield Timeline()
        yield TeamStats(TEAM_STATS, id='stats_ct')
        yield Footer()


    def update_data(self, data:ScoreboardData, ct_stats:list[PlayerStat], t_stats:list[PlayerStat] ):
        self.query_one(ScoreboardTopHeader).update_data(data)
        self.query_one('#stats_t', TeamStats).update_data(t_stats)
        self.query_one('#stats_ct', TeamStats).update_data(ct_stats)
        
if __name__ == "__main__":
    app = ScoreboardApp()
    
    sio = socketio.Client(reconnection_attempts=8)
    @sio.event
    def connect():
        print('connection established')

    @sio.event
    def scoreboard(data):
        round_n = data['currentRound']
        map_name = data['mapName']
        time = '0'
        ct_score = data['counterTerroristScore']
        t_score = data['terroristScore']
        new_data = ScoreboardData(round_n,map_name,time,ct_score,t_score)

        t_stats = list(map(PlayerStat.from_dict, data['TERRORIST']))
        ct_stats = list(map(PlayerStat.from_dict, data['CT']))
        #lock.acquire()
        app.call_from_thread(app.update_data, new_data, ct_stats, t_stats)
        #lock.release()

    @sio.event
    def log(data):
        pass

    @sio.event
    def disconnect():
        print('disconnected from server')

    sio.connect('http://localhost:8080')
    app.run()


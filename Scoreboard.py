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

    def on_mount(self) -> None:
        self.set_interval(1, self.update_data)

    def update_data(self):
        self.counter += 1
        new_data = ScoreboardData(
            str(self.counter + 13), 
            "Overpass", 
            str(self.counter), 
            str(self.counter + 4), 
            str(self.counter + 9)
        )
        self.query_one(ScoreboardTopHeader).update_data(new_data)
        

if __name__ == "__main__":
    app = ScoreboardApp()
    app.run()

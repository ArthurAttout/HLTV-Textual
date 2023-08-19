from __future__ import annotations
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Static, Placeholder

from ScoreboardTopHeader import ScoreboardTopHeader
from TeamStats import TeamStats
from Timeline import Timeline

from TeamStats import PlayerStat

ROWS = [
    PlayerStat("deko",        False, "WP",100,True,1430,4,1,2,87.0),
    PlayerStat("Boombl4",     False,"AWP",100,True,1430,4,1,2,87.0),
    PlayerStat("TRAVIS",      True,"AWP",100,True,1430,4,1,2,87.0),
    PlayerStat("NickelBack",  False,"AWP",100,True,1430,4,1,2,87.0),
    PlayerStat("Forester",    True,"AWP",100,True,1430,4,1,2,87.0),
]


class ScoreboardApp(App):
    CSS_PATH = "Scoreboard.css"
    def compose(self) -> ComposeResult:
        yield Header()
        yield ScoreboardTopHeader()
        yield TeamStats(ROWS)
        yield Timeline()
        yield TeamStats(ROWS)
        yield Footer()


if __name__ == "__main__":
    app = ScoreboardApp()
    app.run()

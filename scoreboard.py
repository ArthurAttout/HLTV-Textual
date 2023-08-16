from __future__ import annotations
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Static, Placeholder

from ScoreboardTopHeader import ScoreboardTopHeader
from TeamStats import TeamStats
from Timeline import Timeline

class ScoreboardApp(App):
    CSS_PATH = "scoreboard.css"
    def compose(self) -> ComposeResult:
        yield Header()
        yield ScoreboardTopHeader()
        yield TeamStats("Team 1 score")
        yield Timeline()
        yield TeamStats("Team 2 score")
        yield Footer()


if __name__ == "__main__":
    app = ScoreboardApp()
    app.run()

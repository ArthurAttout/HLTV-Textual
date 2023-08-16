from __future__ import annotations
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Static, Placeholder


class TeamsScores(Static):
    def compose(self) -> ComposeResult:
        with Container(id="teams-score"):
            yield Static("10",id="score-ct", classes="scoreboard-element")
            yield Static(" - ", id="score-separator", classes="scoreboard-element")
            yield Static("9",id="score-t", classes="scoreboard-element")

class ScoreboardTopHeader(Static):
    def compose(self) -> ComposeResult:
        with Container(id="scoreboard-container"):
            yield Placeholder("R27 - Overpass",classes="scoreboard-element")
            yield TeamsScores()
            yield Placeholder("0:56",classes="scoreboard-element")

class TeamStats(Static):
    def __init__(self, name):
        Static.__init__(self)
        self.custom_name = name

    def compose(self) -> ComposeResult:
        yield Placeholder(self.custom_name)

class Timeline(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder('Timeline')

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

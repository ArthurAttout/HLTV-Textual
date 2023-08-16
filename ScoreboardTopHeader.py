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


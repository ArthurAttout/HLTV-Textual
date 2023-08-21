from __future__ import annotations
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Static, Placeholder
from textual.reactive import reactive

class TeamsScores(Static):
    def __init__(self, data:ScoreboardData):
        Static.__init__(self)
        self.ct_score = reactive(data.ct_score)
        self.t_score = reactive(data.t_score)

    def compose(self) -> ComposeResult:
        with Container(id="teams-score"):
            yield Static("0",id="score-ct", classes="scoreboard-element")
            yield Static(" - ", id="score-separator", classes="scoreboard-element")
            yield Static("0",id="score-t", classes="scoreboard-element")

    def update_data(self, data:ScoreboardData):
        self.query_one("#score-ct", Static).update(data.ct_score)
        self.query_one("#score-t", Static).update(data.t_score)

class ScoreboardTopHeader(Static):
    def __init__(self,data:ScoreboardData):
        Static.__init__(self)
        self.data = data
        
    def compose(self) -> ComposeResult:
        with Container(id="scoreboard-container"):
            yield Static("", id="elem-scoreboard-round", classes="scoreboard-round")
            yield TeamsScores(self.data)
            yield Static("0", id="elem-scoreboard-time", classes="scoreboard-time")
    
    def update_data(self, data:ScoreboardData):
        round_status = f"{data.map_name} - {data.round_number}"
        self.query_one(TeamsScores).update_data(data)
        self.query_one("#elem-scoreboard-time", Static).update(data.time)
        self.query_one("#elem-scoreboard-round", Static).update(round_status)

class ScoreboardData:
    def __init__(self, round_number:int, map_name:str, time:str, ct_score:int, t_score:int):
        self.round_number = str(round_number)
        self.map_name = map_name
        self.time = str(time)
        self.ct_score = str(ct_score)
        self.t_score = str(t_score)
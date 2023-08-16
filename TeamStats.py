from __future__ import annotations
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Static, Placeholder


class TeamStats(Static):
    def __init__(self, name):
        Static.__init__(self)
        self.custom_name = name

    def compose(self) -> ComposeResult:
        yield Placeholder(self.custom_name)
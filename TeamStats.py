from __future__ import annotations
from textual.app import ComposeResult
from textual.widgets import DataTable, Static

COLUMNS_DEFINITION = [
    ("Name", 33),
    ( "Kit", 5),
    ("Weapon", 5),
    ("Health", 5), 
    ("Helmet", 5), 
    ("Money", 5), 
    ("K", 5), 
    ("A", 5), 
    ("D", 5), 
    ("ADR", 6),
]

class TeamStats(Static):
    def __init__(self, stats):
        Static.__init__(self)
        self.custom_stats = stats

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        for column in COLUMNS_DEFINITION:
            table.add_column(column[0], width=column[1])
        table.add_rows(self.custom_stats)
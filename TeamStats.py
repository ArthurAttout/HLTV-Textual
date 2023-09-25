from __future__ import annotations
from textual.app import ComposeResult
from typing import Tuple
from textual.widgets import DataTable, Static

COLUMNS_DEFINITION = [
    ("Name", 33),
    ("Kit", 8),
    ("Weapon", 8),
    ("Health", 7), 
    ("Helmet", 6), 
    ("Money", 13), 
    ("K", 5), 
    ("A", 5), 
    ("D", 5), 
    ("ADR", 6),
]

class PlayerStat:
    def __init__(self, name, has_kit, weapon, health, has_helmet, money, k, a, d, adr):
        self.name = name
        self.has_kit = has_kit
        self.weapon = weapon
        self.health = health
        self.has_helmet = has_helmet
        self.money = money
        self.k = k
        self.a = a
        self.d = d
        self.adr = adr
    
    def to_row(self) -> Tuple:
        return (
            self.name, 
            "V" if self.has_kit else "X",
            self.weapon, 
            self.health, 
            "V" if self.has_helmet else "X", 
            self.money, 
            self.k, self.a, self.d, self.adr
        )
    
    @staticmethod
    def from_dict(data):
        return PlayerStat(
            data['name'],
            False if not('hasDefuseKit' in data) else data['hasDefuseKit'],
            'AK',
            data['hp'],
            data['helmet'],
            data['money'],
            data['score'],
            data['assists'],
            data['deaths'],
            data['damagePrRound']
        )
 

class TeamStats(Static):
    def __init__(self, stats:list[PlayerStat], id:str):
        Static.__init__(self)
        self.custom_stats = stats
        self.id = id

    def compose(self) -> ComposeResult:
        yield DataTable(show_cursor=False)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        for column in COLUMNS_DEFINITION:
            table.add_column(column[0], width=column[1])
        self.update_data(self.custom_stats)

    def update_data(self, data:list[PlayerStat]):
        table = self.query_one(DataTable)
        table.clear()
        table.add_rows(map(lambda entry : entry.to_row(), data))
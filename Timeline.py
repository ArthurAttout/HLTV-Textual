from __future__ import annotations
from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Static, Placeholder
from textual.widget import Widget
import random
from enum import Enum
random.seed(42)

class RoundResult(Enum):
    BOMB_DEFUSED = 1
    BOMB_EXPLODED = 2
    T_SIDE_KILLED = 3
    CT_SIDE_KILLED = 4

class RoundResultComponent(Static):
    
    def __init__(self, result: RoundResult):
        Static.__init__(self)
        self.result = result

    def compose(self) -> ComposeResult:
        if self.result == RoundResult.BOMB_DEFUSED:
            yield Vertical(
                Static("🔧", classes="round-result-cell"),
                Static(classes="round-result-cell")
            )
        elif self.result == RoundResult.T_SIDE_KILLED:
            yield Vertical(
                Static("💀", classes="round-result-cell"),
                Static(classes="round-result-cell")
            )
        elif self.result == RoundResult.BOMB_EXPLODED:
            yield Vertical(
                Static(classes="round-result-cell"),
                Static("💥", classes="round-result-cell")
            )
        elif self.result == RoundResult.CT_SIDE_KILLED:
            yield Vertical(
                Static(classes="round-result-cell"),
                Static("💀", classes="round-result-cell")
            )
        else:
            yield Static("Wtf ?", classes="round-result-cell")

class Timeline(Static):
    def compose(self) -> ComposeResult:
        generator = RoundGenerator(30)
        with Container(id="timeline-group"):
            for result in generator:
               yield RoundResultComponent(result)
    


class RoundGenerator:

    def __init__(self, number_rounds):
        self.number_rounds = number_rounds
        self.current_iteration = 0

    def __next__(self) -> RoundResult:
        return self.next()
    
    def __iter__(self) -> RoundResult:
        return self

    def next(self) -> RoundResult:
        if self.current_iteration < self.number_rounds:
            self.current_iteration = self.current_iteration + 1
            index = random.randint(0,len(RoundResult) - 1)
            return list(RoundResult)[index]
        raise StopIteration()
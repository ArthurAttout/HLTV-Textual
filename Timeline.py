from __future__ import annotations
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Static, Placeholder
import random
random.seed(42)

class Timeline(Static):
    def compose(self) -> ComposeResult:
        with Container(id="timeline-group"):
            generator = RoundGenerator(30)
            for is_ct_win in generator:
                yield Placeholder("CT" if is_ct_win else "T")


class RoundGenerator:

    def __init__(self, number_rounds):
        self.number_rounds = number_rounds
        self.current_iteration = 0
        

    def __next__(self):
        return self.next()
    
    def __iter__(self):
        return self

    def next(self):
        if self.current_iteration < self.number_rounds:
            self.current_iteration = self.current_iteration + 1
            return random.randint(0,10) < 5
        raise StopIteration()
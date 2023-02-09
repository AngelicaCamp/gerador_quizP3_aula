from strategy import Quiz
from enum import Enum



class Linguagem(Quiz):

    def __init__(self, tipo):
        self.tipo = TipoLinguagem


class TipoLinguagem(Enum):
    HTML = 1
    CSS = 2
    JavaScript = 3
    Python = 4





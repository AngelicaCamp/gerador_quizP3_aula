from enum import Enum
from questao import QuestaoFactory
from os import read
import json


class Nivel(Enum):
    INICIANTE = 1
    INTERMEDIARIO = 2
    AVANCADO = 3

class NivelStrategy:
    
    # racebe a resposta do usuário (nível de conhecimento)
    # retorna arquivo json com perguntas, de acordo com nivel informado
    def selecionarQuestoes(self, resposta):
        if resposta == Nivel.INICIANTE.value:
            iniciante = json.load(open("json/iniciante.json",encoding='utf-8'))
            return iniciante

        elif resposta == Nivel.INTERMEDIARIO.value:
            intermediario = json.load(open("json/intermediario.json",encoding='utf-8'))
            return intermediario

        elif resposta == Nivel.AVANCADO.value:
            avancado = json.load(open("json/avancado.json",encoding='utf-8'))
            return avancado
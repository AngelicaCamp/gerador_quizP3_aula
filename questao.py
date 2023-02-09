from enum import Enum


class Questao:
    def __init__(self,pergunta,alternativa,gabarito):
        self.pergunta = pergunta
        self.alternativa = alternativa
        self.gabarito = gabarito


class TipoQuestao(Enum):
    OBJETIVA = 1
    VERDADEIRO_FALSO = 2


class QuestaoVerdadeiroFalso(Questao):
    def __init__(self, pergunta, alternativa, gabarito, tipoQuestao):
        self.tipoQuestao = TipoQuestao.VERDADEIRO_FALSO
        super().__init__(pergunta, alternativa, gabarito)



class QuestaoObjetiva(Questao):
    def __init__(self, pergunta, alternativa, gabarito, tipoQuestao):
        self.tipoQuestao = TipoQuestao.OBJETIVA
        super().__init__(pergunta, alternativa, gabarito)

class QuestaoFactory:

    @staticmethod
    def criarQuestao(tipo: TipoQuestao, questoes):
        if tipo == TipoQuestao.VERDADEIRO_FALSO.value:
            return [QuestaoVerdadeiroFalso(
                pergunta=q['pergunta'],
                gabarito=q['gabarito'],
                tipoQuestao=q['tipoQuestao'], 
                alternativa=q['alternativas']) for q in questoes['true_or_false']]

        if tipo == TipoQuestao.OBJETIVA.value:
            return [QuestaoObjetiva(
                pergunta=q['pergunta'],
                gabarito=q['gabarito'],
                tipoQuestao=q['tipoQuestao'], 
                alternativa=q['alternativas']) for q in questoes['objetiva']]

        return None
    


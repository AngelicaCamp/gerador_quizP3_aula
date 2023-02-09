from nivel import Nivel
from questao import Questao
from questao import TipoQuestao
from questao import QuestaoFactory
from nivel import NivelStrategy
import json


class Aluno:
    def __init__(self,nome,sexo,nivel):
        self.nome = ''
        self.sexo = ''
        self.nivel = Nivel


class Quiz:

    def __init__(self):
        pass

    #verificar qual o nível de conhecimento do aluno
    def verificarNivelAluno(self):
        print(f'===============================================')
        print(f'BEM VINDO(A) AO QUIZ!')
        print(f'Informe seu nível de conhecimento:')
        print(f'1) Iniciante')
        print(f'2) Intermediário')
        print(f'3) Avançado')
        resposta = input()
        self.nivelAluno = int(resposta)

        
    def definirTipoQuestao(self):
        print(f'===============================================')
        print(f'Selecione o tipo de questao desejado:')
        print(f'1) Questão Múltipla - [a,b,c,d]')
        print(f'2) Questão única - [verdadeiro ou falso]')
        resposta = input()
        self.tipoQuestao = int(resposta)


class QuizFacade:


    def __init__(self):
        self.quiz = Quiz()
        self.nivel = NivelStrategy()
        self.questao = QuestaoFactory()


    def iniciar(self):
        self.quiz.verificarNivelAluno()
        self.quiz.definirTipoQuestao()
        questoes = self.nivel.selecionarQuestoes(self.quiz.nivelAluno)
        self.questoes = self.questao.criarQuestao(self.quiz.tipoQuestao, questoes)
        self.mostrarQuestoes()
    

    def mostrarQuestoes(self):
        contador = 0
        for i, q in enumerate(self.questoes):
            print('\n' + '=' * 40 + f'[ Questão {i+1} ]' + '=' * 40)
            print(q.pergunta)
            for altId, alt in enumerate(q.alternativa):
                print(f'{altId + 1}) {alt}')
            res = int(input(f'\nResposta: ')) - 1

            if res == q.gabarito:
                contador = contador + 1

        percentual = contador / len(self.questoes) * 100

        if percentual == 100:
            print(f'Parabéns! Você acertou {percentual:.2f}% das questões do quiz.')
        elif percentual == 0:
            print(f'Você não acertou nenhuma questão. Tente novamente')
            self.iniciar()
        else:
            print(f'Você acertou {percentual:.2f}% das questões do quiz. Continue praticando... ')
            self.iniciar()
             

if __name__ == '__main__':
    
    facade = QuizFacade()
    facade.iniciar()
    


    

    
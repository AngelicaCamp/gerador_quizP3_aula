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
        resposta = 0
        while True:
            print(f'===============================================')
            print(f'BEM VINDO(A) AO QUIZ!')
            print(f'Informe seu nível de conhecimento:')
            print(f'1) Iniciante')
            print(f'2) Intermediário')
            print(f'3) Avançado')
            resposta = int(input('Opção: '))

            if self.validaResposta(resposta, 3):
                break

        self.nivelAluno = resposta

    # define qual o tipo de questão o usuário vai responder 
    def definirTipoQuestao(self):
        resposta = 0
        while True:
            print(f'===============================================')
            print(f'Selecione o tipo de questao desejado:')
            print(f'1) Questão objetiva')
            print(f'2) Questão verdadeiro ou falso')
            resposta = int(input('Opção: '))

            if self.validaResposta(resposta, 2):
                break

        self.tipoQuestao = resposta

    # valida se a opção informada é válida
    def validaResposta(self,res,size):
        if res > 0 and res <= size:
            return True
        else:
            print('\t~> Resposta inválida, tente novamente...')
            return False


class QuizFacade:

    def __init__(self):
        self.quiz = Quiz()
        self.nivel = NivelStrategy()
        self.questao = QuestaoFactory()
        self.responses = []


    def iniciar(self):
        self.quiz.verificarNivelAluno()
        self.quiz.definirTipoQuestao()
        questoes = self.nivel.selecionarQuestoes(self.quiz.nivelAluno)
        self.questoes = self.questao.criarQuestao(self.quiz.tipoQuestao, questoes)
        self.mostrarQuestoes()
    
    # mostra as questões ao usuário
    def mostrarQuestoes(self):
        contador = 0
        resposta = 0

        for i, q in enumerate(self.questoes):
            res=0
            while True:
                print('\n' + '=' * 40 + f'[ Questão {i+1} ]' + '=' * 40)
                print(q.pergunta)

                for altId, alt in enumerate(q.alternativa):
                    print(f'{altId + 1}) {alt}')
                res = int(input(f'\nResposta: '))

                if self.validaResposta(res, len(q.alternativa)):
                    res = res - 1
                    break

            self.responses.append(res)
            if res == q.gabarito:
                contador += 1

        percentual = contador / len(self.questoes) * 100

        if percentual == 100:
            print(f'Parabéns! Você acertou {percentual:.2f}% das questões do quiz.')
        elif percentual == 0:
            print(f'Você não acertou nenhuma questão. Tente novamente')
        else:
            print(f'Você acertou {percentual:.2f}% das questões do quiz. Continue praticando... ')
             
        self.mostraRespostas()

        if percentual != 100:
            print('*'*60)
            res = input('Deseja tentar novamente (S/n)? ')
            if res.lower() == 's' or res == '':
                self.iniciar()

    # mostra respostas ao usuário
    def mostraRespostas(self):
        for i, q in enumerate(self.questoes):
            print('\n' + '=' * 40 + f'[ Gabarito {i+1} ]' + '=' * 40)
            print(q.pergunta)
            for altId, alt in enumerate(q.alternativa):
                if altId == q.gabarito:
                    self.imprimeVerde(f'{altId + 1}) {alt}')
                elif altId == self.responses[i]:
                    self.imprimeVermelho(f'{altId + 1}) {alt}')
                else:
                    print(f'{altId + 1}) {alt}')

    # mostra resposta em vermelho, quando estiver incorreta
    def imprimeVermelho(self, text): 
        print("\033[91m {}\033[00m" .format(text))
    
    # mostra a resposta em verde, quando estiver correta 
    def imprimeVerde(self, text): 
        print("\033[92m {}\033[00m" .format(text))

    def validaResposta(self,res,size):
        if res > 0 and res <= size:
            return True
        else:
            print('\t~> Resposta inválida, tente novamente...')
            return False
    

if __name__ == '__main__':
    
    facade = QuizFacade()
    facade.iniciar()
    


    

    
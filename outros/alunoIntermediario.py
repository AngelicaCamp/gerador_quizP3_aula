from nivel import Aluno

class AlunoIniciante(Aluno):
    
    def __init__(self,nome,idade,sexo,nota):
        self.nota = nota
        Aluno.__init__(self,nome,idade,sexo)


    def calcularPontuacao(self):
        return self.nota * 0.15
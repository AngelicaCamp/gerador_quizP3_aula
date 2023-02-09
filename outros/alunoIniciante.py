from nivel import Aluno

class AlunoIniciante(Aluno):
    
    def __init__(self,nome='',idade=None,sexo=None):
        self.nota = 0
        Aluno.__init__(self,nome,idade,sexo)


    def carregarPerguntas(self):
        return lerJson['iniciante']
class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self):
        print("O professor"+ self.nome+ "está ministrando uma aula sobre ASSUNTO." + self.assunto)

    def mudar_cor(self, nova_cor):
        print("Cor do animal: " + nova_cor)

class Aluno:
    def __init__(self, nome):
      self.nome = nome

    def presenca(self):
        print("O aluno"+ self.nome+ "está presente.")

class Aula:
    def __init__(self,professor, assunto, alunos):
        self.assunto = assunto
        self.professor = professor
        self.alunos = alunos
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        print('Presença na aula sobre' + self.assunto + ' ministrado pelo ' + professor.nome)
        for aluno in self.alunos:
            print(aluno.nome)
          

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos", [])
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

    
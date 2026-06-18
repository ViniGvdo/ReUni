from .pessoa import Pessoa
from .semestre import Semestre

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        self.IRA = 0.0
        self.semestres = []

    def menu_aluno(self):
        while True:
            print("Voce esta no menu do aluno, digite '0' para sair")
            print("1 - Criar novo semestre")
            print("2 - Selecionar Semestre existente")
            print("3 - Relatorio do Aluno")
            status = int(input("Escolha o numero da funcao que deseja executar: "))
            match status:
                case 0:
                    return
                case 1:
                    sem = input("Insira o semestre (ano.digito): ")
                    self.criar_semestre(sem)

                case 2:
                    if self.semestres:
                        print("=== Semestres ===")
                        for semestre in self.semestres:
                            semestre.apresentar_semestre()
                            print()
                
                        sem = input("Qual semestre deseja selecionar?")
                        if self.verificar_semestre(sem):
                            semestre = self.buscar_semestre(sem)
                            semestre.menu_semestre()
                        else: 
                            print("Semestre nao cadastrado") 
                    else:
                        print("Nao ha semestres criados")

                case 3:
                    self.relatorio_aluno()

                case _:
                    print("Funcao invalida")

    """
    Implementar GETTERS E SETTERS de:
        nome
        matricula
        IRA
        semestres(lista)
    """

    def apresentar_aluno(self):
        print(f"Aluno: {self.nome}\nMatricula: {self.matricula}")

    def calcular_IRA(self):
        #Implementar
        pass

    def relatorio_aluno(self):
        print(f"=== Relatorio de {self.nome} ===")
        print(f"Matricula: {self.matricula}")
        print()
        for semestre in self.semestres:
            semestre.relatorio_semestre()
        print(f"=== Relatorio de {self.nome} ===")

    def criar_semestre(self, semestre):
        sem = Semestre(semestre)
        self.semestres.append(sem)

    def verificar_semestre(self, sem):
        for semestre in self.semestres:
            if(semestre.semestre == sem):
                return True
        return False

    def buscar_semestre(self, sem):
        for semestre in self.semestres:
            if(semestre.semestre == sem):
                return semestre

    def deletar_semestre(self, semestre):
        #Implementar 
        pass

from ..models.aluno import Aluno

class System:
    def __init__(self):
        self.alunos = []

    def exibir_alunos(self):
        if(self.alunos):
            print("=== LISTA DOS ALUNOS ===")
            print()
            for aluno in self.alunos:
                aluno.apresentar()
                print()
            return True
        else:
            print("Nenhum aluno cadastrado")
            return False
                
    def menu_geral(self):
        while True:
            print("Voce esta no menu geral, digite '0' para sair")
            print("1 - Selecionar Aluno")
            print("2 - Criar Aluno")
            print("3 - Deletar Aluno")
            status = int(input("Escolha a funcao que deseja executar: "))
            if(status == 1):
                if self.exibir_alunos():
                    matricula = input("Insira a matricula do aluno que voce deseja selecionar\n")
                    if self.verificar_aluno(matricula):
                        aluno = self.buscar_aluno(matricula)
                        aluno.menu_aluno()
                    else:
                        print("Aluno nao cadastrado")
            elif(status == 2):
                self.novo_aluno()
                print("Aluno criado com sucesso!")
                #Implementar uma funcao se o usuario quiser criar e selecionar logo em seguida
            elif(status == 3):
                if self.exibir_alunos():
                    matricula = input("Insira a matricula do aluno que voce deseja selecionar\n")
                    if self.verificar_aluno(matricula):
                        self.deletar_aluno(matricula)
                    else:
                        print("Aluno nao cadastrado")
            elif(status == 0):
                return
            else:
                print("Resposta invalida, tente novamente")

    
    def novo_aluno(self):
        nome = input("Insira o nome do aluno: ")
        matricula = input("Insira a matricula do aluno: ")
        email = input("Insira o email do aluno: ")
        self.criar_aluno(nome, matricula, email)

    def criar_aluno(self, nome, matricula, email):
        aluno = Aluno(nome, matricula, email)
        self.alunos.append(aluno)

    def verificar_aluno(self, matricula):
        for aluno in self.alunos:
            if(aluno.matricula == matricula):
                return True
        return False

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if(aluno.matricula == matricula):
                return aluno


    def deletar_aluno(self, matricula):
        self.alunos.remove(self.buscar_aluno(matricula))




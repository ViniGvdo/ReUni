from ..models.aluno import Aluno

class System:
    def __init__(self):
        self.alunos = []

    def exibir_alunos(self):
        if(self.alunos):
            print("=========================================")
            print("             LISTA DE ALUNOS             ")
            print("=========================================")
            for aluno in self.alunos:
                aluno.apresentar()
                print()
            print("=========================================")
            return True
        else:
            print("Nenhum aluno cadastrado")
            return False
                
    def menu_geral(self):
        while True:
            print()
            print("=========================================")
            print("                MENU GERAL              ")
            print("=========================================")
            print("0 - SAIR")
            print("1 - Criar Aluno")
            print("2 - Selecionar Aluno")
            print("3 - Criar e Selecionar Aluno")
            print("4 - Deletar Aluno")
            print("5 - Listar Alunos")
            print("=========================================")
            status = int(input("Escolha a funcao que deseja executar: "))
            if(status == 1):
                self.novo_aluno()
                print("Aluno criado com sucesso!")
            elif(status == 2):
                if self.exibir_alunos():
                    matricula = input("Insira a matricula do aluno que voce deseja selecionar\n")
                    if self.verificar_aluno(matricula):
                        aluno = self.buscar_aluno(matricula)
                        aluno.menu_aluno()
                    else:
                        print("Aluno nao cadastrado")
            elif(status == 3):
                nome = input("Insira o nome do aluno: ")
                matricula = input("Insira a matricula do aluno: ")
                email = input("Insira o email do aluno: ")
                self.criar_aluno(nome, matricula, email)
                print("Aluno criado com sucesso!")
                aluno = self.buscar_aluno(matricula)
                aluno.menu_aluno()

            elif(status == 4):
                if self.exibir_alunos():
                    matricula = input("Insira a matricula do aluno que voce deseja selecionar\n")
                    if self.verificar_aluno(matricula):
                        self.deletar_aluno(matricula)
                    else:
                        print("Aluno nao cadastrado")
            elif(status == 5):
                self.exibir_alunos()
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




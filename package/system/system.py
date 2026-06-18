from ..models.aluno import Aluno

class System:
    def __init__(self):
        self.alunos = []

    def exibir_alunos(self):
        if(self.alunos):
            print("=== LISTA DOS ALUNOS ===")
            print()
            for aluno in self.alunos:
                aluno.apresentar_aluno()
                print()
            return True
        else:
            print("Nenhum aluno cadastrado")
            return False
                
    def menu_geral(self):
        while True:
            print("Voce esta no menu geral, digite '0' para sair")
            status = input("Digite 's' para selecionar um aluno existente, 'c' para criar um novo aluno: ")
            if(status == 's'):
                if self.exibir_alunos():
                    matricula = input("Insira a matricula do aluno que voce deseja selecionar\n")
                    aluno = self.buscar_aluno(matricula)
                    aluno.menu_aluno()
            elif(status == 'c'):
                self.novo_aluno()
                print("Aluno criado com sucesso!")
                #Implementar uma funcao se o usuario quiser criar e selecionar logo em seguida
            elif(status == '0'):
                return
            else:
                print("Resposta invalida, tente novamente")

    
    def novo_aluno(self):
        nome = input("Insira o nome do aluno: ")
        matricula = input("Insira a matricula do aluno: ")
        self.criar_aluno(nome, matricula)

    def criar_aluno(self, nome, matricula):
        aluno = Aluno(nome, matricula)
        self.alunos.append(aluno)

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if(aluno.matricula == matricula):
                return aluno


    def deletar_aluno(self, matricula):
        #Implementar
        pass




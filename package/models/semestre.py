from .materia import Materia
from .professor import Professor

class Semestre:
    def __init__(self, semestre:str, periodo:int):
        self.__semestre = semestre
        self.__periodo = periodo
        self.materias = []

    #GETTERS E SETTERS

    @property
    def semestre(self):
        return self.__semestre
    
    @semestre.setter
    def semestre(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__semestre = value

    @property
    def periodo(self):
        return self.__periodo
    
    @periodo.setter
    def periodo(self, value):
        if not isinstance(value, int):
            raise ValueError("O valor deve ser um inteiro")
        if value < 0:
            raise ValueError("O valor nao pode ser negativo")
        if value > 21:
            raise ValueError("O valor nao pode ser maior que 21")
        self.__periodo = value

    #MÉTODOS

    def menu_semestre(self):
        while True:
            print("Voce esta no menu do semestre, digite '0' para sair")
            print("1 - Criar nova Materia")
            print("2 - Selecionar Materia")
            print("3 - Criar e Selecionar Materia")
            print("4 - Deletar Materia")
            print("5 - Listar Materias")
            status = int(input("Escolha o numero da funcao que deseja executar: "))
            match status:
                case 0:
                    return
                
                case 1:
                    nome = input("Nome da materia: ")
                    codigo = input("Codigo: ")
                    carga_horaria = int(input("Carga Horaria em horas: "))
                    horario = input("Horario: ")
                    nome_professor = input("Nome do Professor: ")
                    email_professor = input("Email do professor: ")
                    departamento_professor = input("Departamento do professor: ")
                    professor = Professor(nome_professor, email_professor, departamento_professor)
                    turma = input("Turma: ")
                    self.criar_materia(nome, codigo, carga_horaria, horario, professor, turma)

                case 2:
                    if self.materias:
                        print("=== Lista de Materias ===")
                        for materia in self.materias:
                            materia.apresentar_materia()
                            print()

                        codigo_materia = input("Digite o codigo da materia que deseja selecionar: ")
                        if self.verificar_materia(codigo_materia):
                            materia = self.buscar_materia(codigo_materia)
                            materia.menu_materia()  
                        else: 
                            print("Codigo de Materia invalido")

                    else:
                        print("Nao ha semestres criados")

                case 3:
                    nome = input("Nome da materia: ")
                    codigo = input("Codigo: ")
                    carga_horaria = int(input("Carga Horaria em horas: "))
                    horario = input("Horario: ")
                    nome_professor = input("Nome do Professor: ")
                    email_professor = input("Email do professor: ")
                    departamento_professor = input("Departamento do professor: ")
                    professor = Professor(nome_professor, email_professor, departamento_professor)
                    turma = input("Turma: ")
                    self.criar_materia(nome, codigo, carga_horaria, horario, professor, turma)
                    materia = self.buscar_materia(codigo)
                    materia.menu_materia()

                case 4:
                    if self.materias:
                        print("=== Lista de Materias ===")
                        for materia in self.materias:
                            materia.apresentar_materia()
                            print()

                        codigo_materia = input("Digite o codigo da materia que deseja deletar: ")
                        if self.verificar_materia(codigo_materia):
                            self.deletar_materia(codigo_materia)
                        else: 
                            print("Codigo de Materia invalido")

                    else:
                        print("Nao ha semestres criados")

                case 5:
                    if self.materias:
                        print("=== Lista de Materias ===")
                        for materia in self.materias:
                            materia.apresentar_materia()
                            print()
                    else:
                        print("Nao ha semestres criados")

                case _:
                    print("Funcao invalida")


    def apresentar_semestre(self):
        print(f"{self.semestre} ({self.periodo})")

    def relatorio_semestre(self):
        print(f"=== {self.semestre} ===")
        for materia in self.materias:
            materia.relatorio_materia()
        print("====== ======")
        print()

    def criar_materia(self, nome, codigo, carga_horaria, horario, professor, turma):
        materia = Materia(nome, codigo, carga_horaria, horario, professor, turma)
        self.materias.append(materia)

    def verificar_materia(self, codigo):
        for materia in self.materias:
            if(materia.codigo == codigo):
                return True
        return False

    def buscar_materia(self, codigo):
        for materia in self.materias:
            if(materia.codigo == codigo):
                return materia


    def deletar_materia(self, codigo):
        self.materias.remove(self.buscar_materia(codigo))

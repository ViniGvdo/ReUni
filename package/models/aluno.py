from .pessoa import Pessoa
from .semestre import Semestre

class Aluno(Pessoa):
    def __init__(self, nome:str, matricula:str, email:str):
        self.__nome = nome
        self.__matricula = matricula
        self.__email = email
        self.__IRA = 0.0
        self.semestres = []

    #GETTERS E SETTERS

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__nome = value

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, value):
        if not isinstance(value, str):
            raise TypeError("O valor deve ser uma string.")
        self.__matricula = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__email = value

    @property
    def IRA(self):
        return self.__IRA
    
    @IRA.setter
    def IRA(self, value):
        if not isinstance(value, float):
            raise TypeError("O valor deve ser um numero flutuante")
        if value < 0:
            raise ValueError("O valor nao pode ser negativo")
        if value > 5.0:
            raise ValueError("O valor nao pode ser maior que 5.0")
        self.__IRA = value

    #MÉTODOS

    def menu_aluno(self):
        while True:
            print()
            print("=========================================")
            print("                MENU ALUNO               ")
            print("=========================================")
            print(f"[{self.nome}]")
            print("0 - VOLTAR")
            print("1 - Criar novo Semestre")
            print("2 - Selecionar Semestre existente")
            print("3 - Criar e Selecionar Semestre")
            print("4 - Deletar semestre")
            print("5 - Listar Semestres")
            print("6 - Relatorio do Aluno")
            print("=========================================")
            status = int(input("Escolha o numero da funcao que deseja executar: "))
            match status:
                case 0:
                    return
                case 1:
                    sem = input("Insira o semestre (ano.digito): ")
                    periodo = int(input("Qual o numero do periodo? "))
                    self.criar_semestre(sem, periodo)

                case 2:
                    if self.semestres:
                        self.listar_semestres()
                
                        sem = input("Qual semestre deseja selecionar? ")
                        if self.verificar_semestre(sem):
                            semestre = self.buscar_semestre(sem)
                            semestre.menu_semestre()
                        else: 
                            print("Semestre nao cadastrado") 
                    else:
                        print("Nao ha semestres criados")

                case 3:
                    sem = input("Insira o semestre (ano.digito): ")
                    periodo = int(input("Qual o numero do periodo? "))
                    self.criar_semestre(sem, periodo)
                    semestre = self.buscar_semestre(sem)
                    semestre.menu_semestre()

                case 4:
                    if self.semestres:
                        self.listar_semestres()
                        sem = input("Qual semestre deseja deletar? ")
                        if self.verificar_semestre(sem):
                            self.deletar_semestre(sem)
                        else: 
                            print("Semestre nao cadastrado") 
                    else:
                        print("Nao ha semestres criados")

                case 5:
                    if self.semestres:
                        self.listar_semestres() 
                    else:
                        print("Nao ha semestres criados")

                case 6:
                    self.relatorio_aluno()

                case _:
                    print("Funcao invalida")

    def listar_semestres(self):
        print("=========================================")
        print("            LISTA DE SEMESTRES           ")
        print("=========================================")
        for semestre in self.semestres:
            semestre.apresentar_semestre()
            print()
        print("=========================================")

    def apresentar(self):
        self.calcular_IRA()
        print(f"Aluno: {self.nome}\nMatricula: {self.matricula}\nEmail: {self.email}\nIRA: {self.IRA}")

    def calcular_IRA(self):
        soma = 0.0
        dividir = 0.0

        equivalencia = 0.0
        credito = 0.0
        nsem = 0.0

        converter = {"SS": 5, "MS": 4, "MM": 3, "MI": 2, "II": 1, "SR": 0, "XX": 0}

        for semestre in self.semestres:
            if semestre.periodo <= 6:
                nsem = semestre.periodo
            else:
                nsem = 6
            if semestre.materias:
                for materia in semestre.materias:
                    credito = materia.carga_horaria / 15
                    equivalencia = converter[materia.mencao]
                    soma += equivalencia * credito * nsem
                    dividir += credito * nsem
        if dividir == 0.0:
            self.IRA = 0.0
        else:
            self.IRA = soma / dividir


    def relatorio_aluno(self):
        print("=========================================")
        print("           RELATORIO DO ALUNO            ")
        print("=========================================")
        print()
        print(f"Aluno: {self.nome}")
        print(f"Matricula: {self.matricula}")
        self.calcular_IRA()
        print(f"IRA: {self.IRA}")
        print()
        if self.semestres:
            for semestre in self.semestres:
                print("-----------------------------------------")
                print(f"Semestre Letivo: {semestre.semestre}")
                print("-----------------------------------------")
                semestre.relatorio_semestre()
        print("=========================================")

    def criar_semestre(self, semestre, periodo):
        sem = Semestre(semestre, periodo)
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
        self.semestres.remove(self.buscar_semestre(semestre))

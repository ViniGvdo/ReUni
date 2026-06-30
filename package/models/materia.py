from .professor import Professor
from .avaliacao import Avaliacao
from .falta import Falta

class Materia:
    def __init__(self, nome:str, codigo:str, carga_horaria:int, horario:str, professor:Professor, turma:int):
        self.__nome = nome
        self.__codigo = codigo
        self.__carga_horaria = carga_horaria
        self.__horario = horario
        self.__professor = professor
        self.__turma = turma
        self.__nota = 0
        self.__mencao = "XX"
        self.faltas = []
        self.avaliacoes = []

    #GETTERS E SETTERS
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise TypeError("O valor deve ser uma string.")
        self.__nome = value

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, value):
        if not isinstance(value, str):
            raise TypeError("O valor deve ser uma string.")
        self.__codigo = value

    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, value):
        if not isinstance(value, int):
            raise TypeError("O valor deve ser um número inteiro.")
        if value not in [15, 30, 45, 60, 75, 90, 105, 120]:
            raise ValueError("O valor deve ser: 15, 30, 45, 60, 75, 90, 105 ou 120")
        self.__carga_horaria = value

    @property
    def horario(self):
        return self.__horario
    
    @horario.setter
    def horario(self, value):
        if not isinstance(value, str):
            raise TypeError("O valor deve ser uma string.")
        self.__horario = value

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, value):
        if not isinstance(value, Professor):
            raise TypeError("O valor deve ser um Professor.")
        self.__professor = value

    @property
    def turma(self):
        return self.__turma
    
    @turma.setter
    def turma(self, value):
        if not isinstance(value, int):
            raise TypeError("O valor deve ser um número inteiro.")
        if value < 0:
            raise ValueError("O número não pode ser negativo.")
        self.__turma = value

    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, value):
        if not isinstance(value, float):
            raise TypeError("O valor deve ser um número flutuante.")
        if value <= 0:
            raise ValueError("O número não pode ser negativo.")
        if value > 10.0:
            raise ValueError("O número não pode ser maior que 10.0.")
        self.__nota = value

    @property
    def mencao(self):
        return self.__mencao
    
    @mencao.setter
    def mencao(self, value):
        if not isinstance(value, str):
            raise TypeError("O valor deve ser uma string.")
        if value not in ["SR", "II", "MI", "MM", "MS", "SS", "XX"]:
            raise ValueError("O valor deve ser: SR, II, MI, MM, MS, SS ou XX")
        self.__mencao = value

    #MÉTODOS

    def menu_materia(self):
        while True:
            print()
            print("=========================================")
            print("               MENU MATERIA              ")
            print("=========================================")
            print(f"[{self.nome}]")
            print("0 - VOLTAR")
            print("1 - Relatorio da Materia")
            print("2 - Registrar Falta")
            print("3 - Listar Faltas")
            print("4 - Apagar Falta")
            print("5 - Relatorio de Frequencia")
            print("6 - Criar avaliacao")
            print("7 - Listar Avaliacoes")
            print("8 - Apagar Avaliacao")
            print("9 - Relatorio avaliacoes")
            print("10 - Informacoes do Professor")
            print("=========================================")

            status = int(input("Escolha o numero da funcao que deseja executar: "))
            match status:
                case 0:
                    return
                
                case 1:
                    self.relatorio_materia()

                case 2:
                    qtd = int(input("Quantas faltas deseja registrar? "))
                    data = input("Data 'dia/mes/ano': ")
                    self.criar_falta(qtd, data)

                case 3:
                    self.listar_faltas()

                case 4:
                    self.listar_faltas()
                    if self.faltas:
                        id = int(input("Escolha o id da falta que deseja excluir: "))
                        if self.verificar_falta(id):
                            self.deletar_falta(id)
                        else:
                            print("id de Falta invalido")
                    

                case 5:
                    self.relatorio_frequencia()

                case 6:
                    nome = input("Nome: ")
                    nota = float(input("Nota: "))
                    peso = float(input("Peso: "))
                    data = input("Data 'dia/mes/ano': ")
                    self.criar_avaliacao(nome, nota, peso, data)

                case 7:
                    if self.avaliacoes:
                        print("=========================================")
                        print("            LISTA DE AVALIACOES          ")
                        print("=========================================")
                        self.listar_avaliacoes()
                        print("=========================================")
                    else:
                        print("Nao ha avaliacoes registradas")

                case 8:
                    if self.avaliacoes:
                        print("=========================================")
                        print("            LISTA DE AVALIACOES          ")
                        print("=========================================")
                        self.listar_avaliacoes()
                        print("=========================================")
                        id = int(input("Escolha o id da avaliacao que deseja excluir: "))
                        if self.verificar_avaliacao(id):
                            self.deletar_avaliacao(id)
                        else:
                            print("id de Avaliacao invalido")
                    else: 
                        print("Nao ha avaliacoes registradas")

                case 9:
                    self.relatorio_avaliacoes()

                case 10:
                    print("=========================================")
                    print("             SOBRE O PROFESSOR           ")
                    print("=========================================")
                    self.professor.apresentar()
                    print("=========================================")

                case _:
                    print("Funcao Invalida")

    def apresentar_materia(self):
        print(f"{self.__nome}\nCodigo: {self.__codigo}")

    def relatorio_materia(self):
        print("=========================================")
        print("           RELATORIO DA MATERIA          ")
        print("=========================================")
        print(f"[{self.nome}]")
        print(f"Codigo: {self.__codigo}")
        print(f"Carga Horaria: {self.__carga_horaria}")
        print(f"Horario: {self.__horario}")
        self.__professor.apresentar()
        print(f"Turma: {self.__turma}")
        print()
        print("[NOTAS]")
        print(f"Mencao: {self.mencao}")
        print(f"Nota final: {self.nota}")
        print()
        print("AVALIACOES")
        self.listar_avaliacoes()
        print("=========================================")

    def listar_avaliacoes(self):
        if self.avaliacoes:
            for avaliacao in self.avaliacoes:
                avaliacao.apresentar_avaliacao()

    def relatorio_avaliacoes(self):
        if self.avaliacoes:
            print("=========================================")
            print("         RELATORIO DE RENDIMENTO         ")
            print("=========================================")
            print(f"Nota: {self.nota}")
            print(f"Mencao: {self.mencao}")
            print()
            print("[Avaliacoes]")
            for avaliacao in self.avaliacoes:
                avaliacao.apresentar_avaliacao()
            print("=========================================")
        else:
            print("Nao ha avaliacoes registradas")

    def calcular_max_faltas(self):
        return int(self.__carga_horaria * 0.25) #Levando em conta que o maximo de faltas é 25%

    def criar_falta(self, qtd, data):
        falta = Falta(qtd, data)
        self.faltas.append(falta)

    def verificar_falta(self, id):
        for falta in self.faltas:
            if id == falta.id:
                return True
        return False
    
    def buscar_falta(self, id):
        for falta in self.faltas:
            if id == falta.id:
                return falta

    def deletar_falta(self, id):
        self.faltas.remove(self.buscar_falta(id))

    def calcular_faltas(self):
        num_faltas = 0
        for falta in self.faltas:
            num_faltas += falta.qtd
        return num_faltas
    
    def listar_faltas(self):
        if self.faltas:
            print("=========================================")
            print("             LISTA DE FALTAS             ")
            print("=========================================")
            for falta in self.faltas:
                falta.exibir_falta()
            print("=========================================")
        else:
            print("Nao ha faltas cadastradas")

    def relatorio_frequencia(self):
        print("=========================================")
        print("          RELATORIO DE FREQUENCIA        ")
        print("=========================================")
        print()
        print(f"Faltas: {self.calcular_faltas()}/{self.calcular_max_faltas()}\n")
        for falta in self.faltas:
            falta.exibir_falta()
        print()
        print("=========================================")

    def calcular_nota(self):
        nota = 0.0
        peso_total = 0
        for avaliacao in self.avaliacoes:
            nota += avaliacao.nota * avaliacao.peso
            peso_total += avaliacao.peso

        self.__nota = nota / peso_total

    def calcular_mencao(self):
        if(self.calcular_faltas() > self.calcular_max_faltas()):
            self.mencao = "SR"
        else:
            if(self.__nota < 3.0):
                self.mencao = "II"
            elif(self.__nota >= 3.0 and self.__nota < 5.0):
                self.mencao = "MI"
            elif(self.__nota >= 5.0 and self.__nota < 7.0):
                self.mencao = "MM"
            elif(self.__nota >= 7.0 and self.__nota < 9.0):
                self.mencao = "MS"
            elif(self.__nota >= 9.0):
                self.mencao = "SS"

    def criar_avaliacao(self, nome, nota, peso, data):
        avaliacao = Avaliacao(nome, nota, peso, data)
        self.avaliacoes.append(avaliacao)
        self.calcular_nota()
        self.calcular_mencao()

    def verificar_avaliacao(self, id):
        for avaliacao in self.avaliacoes:
            if id == avaliacao.id:
                return True
        return False
    
    def buscar_avaliacao(self, id):
        for avaliacao in self.avaliacoes:
            if id == avaliacao.id:
                return avaliacao

    def deletar_avaliacao(self, id):
        self.avaliacoes.remove(self.buscar_avaliacao(id))

    


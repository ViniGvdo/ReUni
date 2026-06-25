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
            print("Voce esta no menu da materia, digite '0' para sair")
            print("1 - Relatorio da Materia")
            print("2 - Registrar Falta")
            print("3 - Relatorio de Frequencia")
            print("4 - Criar avaliacao")
            print("5 - Relatorio avaliacoes")

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
                    self.relatorio_frequencia()

                case 4:
                    nome = input("Nome: ")
                    nota = float(input("Nota: "))
                    peso = float(input("Peso: "))
                    data = input("Data 'dia/mes/ano': ")
                    self.criar_avaliacao(nome, nota, peso, data)

                case 5:
                    self.relatorio_avaliacoes()

                case _:
                    print("Funcao Invalida")

    def apresentar_materia(self):
        print(f"{self.__nome}\nCodigo: {self.__codigo}")

    def relatorio_materia(self):
        print(f"=== {self.__nome} ===")
        print(f"Codigo: {self.__codigo}")
        print(f"Carga Horaria: {self.__carga_horaria}")
        print(f"Horario: {self.__horario}")
        self.__professor.apresentar()
        print(f"Turma: {self.__turma}")
        self.relatorio_avaliacoes()
        self.relatorio_frequencia()
        print(f"=== {self.__nome} ===")
        print()

    def relatorio_avaliacoes(self):
        if self.avaliacoes:
            print(f"Nota: {self.nota}")
            print(f"Mencao: {self.mencao}")
            print("=== Avaliacoes ===")
            for avaliacao in self.avaliacoes:
                avaliacao.apresentar_avaliacao()
            print("======== = ========")

    def calcular_max_faltas(self):
        return int(self.__carga_horaria * 0.25) #Levando em conta que o maximo de faltas é 25%

    def criar_falta(self, qtd, data):
        falta = Falta(qtd, data)
        self.faltas.append(falta)

    def calcular_faltas(self):
        num_faltas = 0
        for falta in self.faltas:
            num_faltas += falta.qtd
        return num_faltas

    def relatorio_frequencia(self):
        print("\n=== RELATORIO DE FREQUENCIA ===")
        print(f"Faltas: {self.calcular_faltas()}/{self.calcular_max_faltas()}\n")
        for falta in self.faltas:
            falta.exibir_falta()
        print("=== ========================= ===")

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

    def deletar_avaliacao(self, id):
        #Implementar
        pass

    


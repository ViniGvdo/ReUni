from .professor import Professor
from .avaliacao import Avaliacao
from .falta import Falta

class Materia:
    def __init__(self, nome, codigo, carga_horaria, horario, professor, turma):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.horario = horario
        self.professor = professor
        self.turma = turma
        self.nota = 0
        self.mencao = "XX"
        self.faltas = []
        self.avaliacoes = []

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
        print(f"{self.nome}\nCodigo: {self.codigo}")

    def relatorio_materia(self):
        print(f"=== {self.nome} ===")
        print(f"Codigo: {self.codigo}")
        print(f"Carga Horaria: {self.carga_horaria}")
        print(f"Horario: {self.horario}")
        print(f"Professor: {self.professor.nome}")
        print(f"Email do professor: {self.professor.email}")
        print(f"Turma: {self.turma}")
        self.relatorio_avaliacoes()
        self.relatorio_frequencia()
        print(f"=== {self.nome} ===")
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
        return int(self.carga_horaria * 0.25) #Levando em conta que o maximo de faltas é 25%

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

        self.nota = nota / peso_total

    def calcular_mencao(self):
        if(self.calcular_faltas() > self.calcular_max_faltas()):
            self.mencao = "SR"
        else:
            if(self.nota < 3.0):
                self.mencao = "II"
            elif(self.nota >= 3.0 and self.nota < 5.0):
                self.mencao = "MI"
            elif(self.nota >= 5.0 and self.nota < 7.0):
                self.mencao = "MM"
            elif(self.nota >= 7.0 and self.nota < 9.0):
                self.mencao = "MS"
            elif(self.nota >= 9.0):
                self.mencao = "SS"

    def criar_avaliacao(self, nome, nota, peso, data):
        avaliacao = Avaliacao(nome, nota, peso, data)
        self.avaliacoes.append(avaliacao)
        self.calcular_nota()
        self.calcular_mencao()

    def deletar_avaliacao(self, id):
        #Implementar
        pass

    """
    Implementar GETTERS E SETTERS de:
        nome
        codigo 
        CH
        horario
        turma
        nota
        mencao
        professor
    """


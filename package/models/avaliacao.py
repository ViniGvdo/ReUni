class Avaliacao:
    def __init__(self, nome, nota, peso, data):
        self.nome = nome
        self.nota = nota
        self.peso = peso
        self.data = data
        self.id = nome + data

    def apresentar_avaliacao(self):
        print(f"{self.data} - {self.nome} (peso {self.peso}): {self.nota}")

    """
    Implementar GETTERS E SETTERS de:
        nome
        nota
        peso
        data
        id
    """


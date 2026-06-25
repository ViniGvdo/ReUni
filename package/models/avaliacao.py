class Avaliacao:
    def __init__(self, nome:str, nota:float, peso:float, data:str):
        self.__nome = nome
        self.__nota = nota
        self.__peso = peso
        self.__data = data
        self.__id = nome + data

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
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, value):
        if not isinstance(value, float):
            raise TypeError("O valor deve ser um número flutuante.")
        if value < 0:
            raise ValueError("O número não pode ser negativo.")
        self.__peso = value

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__data = value

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__id = value

    #MÉTODOS

    def apresentar_avaliacao(self):
        print(f"{self.data} - {self.nome} (peso {self.peso}): {self.nota}")



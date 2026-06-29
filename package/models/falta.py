class Falta:
    def __init__(self, qtd:int, data:str):
        self.qtd = qtd
        self.data = data
        #Fazer um atributo de classe para criar um id depois

    #GETTERS E SETTERS

    @property
    def qtd(self):
        return self.__qtd
    
    @qtd.setter
    def qtd(self, value):
        if not isinstance(value, int):
            raise TypeError("O valor deve ser um número inteiro.")
        if value < 0:
            raise ValueError("O número não pode ser negativo.")
        self.__qtd = value

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__data = value

    #MÉTODOS

    def exibir_falta(self):
        print(f"{self.data}: {self.qtd} faltas")

    
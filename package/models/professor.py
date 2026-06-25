from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, email, departamento):
        self.__nome = nome
        self.__email = email
        self.__departamento = departamento

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
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__email = value

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, value):
        if not isinstance(value, str):
            raise ValueError("O valor deve ser uma string")
        self.__departamento = value

    #MÉTODOS

    def apresentar(self):
        print(f"Professor: {self.nome}")
        print(f"Email do professor: {self.email}")

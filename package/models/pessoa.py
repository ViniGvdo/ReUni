from abc import ABC, abstractmethod

class Pessoa(ABC):

    #GETTERS E SETTERS

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, value):
        pass

    @property
    @abstractmethod
    def email(self):
        pass

    @email.setter
    @abstractmethod
    def email(self, value):
        pass

    #MÉTODOS

    @abstractmethod
    def apresentar(self):
        pass
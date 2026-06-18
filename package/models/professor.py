from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, email, siape, departamento):
        super().__init__(nome, email=email)
        self.siape = siape
        self.departamento = departamento


    """
    Implementar GETTERS E SETTERS de:
        nome
        email
        siape
        departamento
    """
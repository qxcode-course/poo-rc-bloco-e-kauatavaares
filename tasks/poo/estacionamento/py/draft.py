from abc import ABC, abstractmethod

class veiculo(ABC):
    def __init__(self, id: str, entrada: int , tipo: str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo
    @abstractmethod
    def calcularValor(self):
        pass
    def __str__(self):
        return f"{self.id}, {self.tipo}, {self.entrada}."
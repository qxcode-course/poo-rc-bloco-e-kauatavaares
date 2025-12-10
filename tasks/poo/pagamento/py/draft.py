from abc import ABC, abstractmethod

class MetodosPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass

class Metodopix(MetodosPagamento):
    def __init__(self, chave: str):
        self.chave = chave
    def processar_pagamento(self, valor: float):
        print(f"pagamento chave {self.chave}, valor {valor} com pix")

class Metodocartão(MetodosPagamento):
    def __init__(self, numero: float, nome_titular: str, limite_disponivel: float):
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel
    def processar_pagamento(self, valor: float):
        if valor > self.limite_disponivel:
            print("fail: limite ultrapasssado!")
        else:
            pass


class Pagamento:
    def __init__(self, valor: float, descricao: str, metodo: MetodosPagamento):
        self.valor = valor
        self.descricao = descricao
        self.metodo = metodo
    def pagar(self):
        self.metodo.processar_pagamento(self.valor)



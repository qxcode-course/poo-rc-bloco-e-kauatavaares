from abc import ABC, abstractmethod

class Pagamento:
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao
    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("Valor negativo")
    def resumo(self):
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero, nome_titu, limite_disp):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titu = nome_titu
        self.limite_disp = limite_disp

    def processar(self):
        if self.valor > self.limite_disp:
            raise Exception(f"Limite insuficiente no cartão")
        else:
            self.limite_disp -= self.valor
            print(f"Pagamento aprovado")

class Pix(Pagamento):
    def __init__(self, valor, descricao, chave, banco):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"Pix enivado via {self.banco} usando a chave {self.chave}")

class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras, vencimento):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        print(f"Boleto gerado. Aguardando pagamento.....")

def processar_pagamento(pagamento = Pagamento):
    try:
         pagamento.validar_valor()
         pagamento.resumo()
         pagamento.processar()
    except Exception as e:
        print(e)

pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    CartaoCredito(400, "Ténis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700)
]
for p in pagamentos:
    processar_pagamento(p)


from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str,tipo: str, entrada: int):
        self.id = id
        self.tipo = tipo
        self.entrada = entrada
    @abstractmethod
    def calcularValor(self):
        pass
    def __str__(self):
        id = self.id.rjust(10,"_")
        tipo = self.tipo.rjust(10, "_")
        return f"{tipo} : {id} : {self.entrada}"

class Bike(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self, exit: int = 0):
        return f"{3:.2f}"

class Moto(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self, exit: int):
        valor = (exit - self.entrada) / 20
        return f"{valor:.2f}"

class Carro(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self, exit: int):
        valor = (exit-self.entrada) /10
        if valor > 5:
            return f"{valor:.2f}"
        else:
            return f"{5:.2f}"


class Estacionamento:
    def __init__(self):
        self.lista: list[Veiculo] = []
        self.hora = 0

    def getHora(self):
        return self.hora

    def passarTempo(self, tempo: int):
        self.hora += tempo

    def Estacionar(self, veiculo: Veiculo):
        self.lista.append(veiculo)

    def procurar(self, id: str) -> Veiculo | None:
        for veiculo in self.lista:
            if veiculo.id == id:
                return veiculo
        return None

    def pagar(self, veiculo: Veiculo):
        entrada  = veiculo.entrada
        saida = self.getHora()
        valor = veiculo.calcularValor(saida)
        return f"{veiculo.tipo} chegou {entrada} saiu {saida}. Pagar R$ {valor}"

    def criarVeiculo(self, tipo: str, id: str):
        if tipo == "bike":
            return Bike(id, "Bike", self.getHora())
        elif tipo == "moto":
            return Moto(id, "Moto", self.getHora())
        elif tipo == "carro":
            return Carro(id, "Carro", self.getHora())


    def __str__(self):
        lista = "\n".join([str(x) for x in self.lista])
        if not lista:
            return f"Hora atual: {self.hora}"
        return f"{lista}\nHora atual: {self.hora}"




def main():
    estacionamento = Estacionamento()
    while True:
        line= input()
        print("$" + line)
        args = line.split()
        cmd = args[0]
        if cmd == "end":
            break
        elif cmd == "show":
            print(estacionamento)
        elif cmd == "tempo":
            estacionamento.passarTempo(int(args[1]))
        elif cmd == "estacionar":
            _, tipo, id = args
            veiculo = estacionamento.criarVeiculo(tipo, id)
            estacionamento.Estacionar(veiculo)
        elif cmd == "pagar":
            id = args[1]
            veiculo = estacionamento.procurar(id)
            if veiculo:
                print(estacionamento.pagar(veiculo))
                estacionamento.lista.remove(veiculo)

main()
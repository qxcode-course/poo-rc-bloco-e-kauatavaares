from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.name}!")

    def fazer_som(self):
        pass

    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, name: str):
        super(). __init__(name)

    def fazer_som(self):
        print("WRAAAAAAU")

    def mover(self):
        print("O leao é o rei da floresta!!")

class Elefante(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def fazer_som(self):
        print("PRRRRRR (SOM DA TROMBA)")

    def mover(self):
        print("O elefante é gigantesco!!")

class Cobra(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def fazer_som(self):
        print("Sssssss...")

    def mover(self):
        print("A cobra é um animal venenoso!!!")


def apresentar(animal = Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print("Tipo do animal:", type(animal).__name__)
    print("-" * 30)


if __name__ == "__main__":
    animais = [
        Leao("Mufasa"),
        Elefante("Elly"),
        Cobra("Nagini")
    ]
    for a in animais:
        apresentar(a)


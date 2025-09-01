# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
        self.size = beverage.get_size()

    def pretty_print(self)-> str:
        lista = self.get_description().split(",")
        unicos= list(dict.fromkeys(lista[1:]))
        texto = lista[0]
        for i in unicos:
            cant = lista.count(i)
            if cant == 1:
                texto= texto + ", "+ i
            elif cant == 2:
                texto= texto + ", Double "+i
            elif cant == 3:
                texto= texto + ", Triple "+i
            else:
                texto= texto + ", "+ str(cant)+"x"+i
        return texto

    @abstractmethod
    def get_description(self) -> str:
        pass

# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20

class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
    # costo Tall 0.10, Grande 0.15, Venti 0.20
        costo = [0.10, 0.15 , 0.20]
        if self.size == "Tall":
            return self._beverage.cost() + costo[0]
        elif self.size == "Grande":
            return self._beverage.cost() + costo[1]
        else:
            return self._beverage.cost() + costo[2]      
              
class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramelo a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20
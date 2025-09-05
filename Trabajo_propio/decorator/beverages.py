# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod


# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """

    def __init__(self, description: str, size: str):
        self.sizes = ["Tall", "Grande", "Venti"]
        self.description = description
        self.size = size


    """ def pretty_print(self)-> str:
        return self.description """

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return self.description


    def set_size(self, size) -> None:
        """
        Establece el tamaño de la bebida.
        """
        if size not in self.get_available_sizes():
            raise ValueError("Tamaño no disponible")
        self.size = size


    def get_size(self) -> str:
        """
        Devuelve el tamaño de la bebida.
        """
        return self.size


    def get_available_sizes(self) -> list[str]:
        """
        Devuelve una lista de los tamaños disponibles para la bebida.
        """
        return self.sizes


    @abstractmethod
    def cost(self) -> float:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida.
        """
        pass


# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__("Café de la Casa", "Tall")

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__("Café Dark Roast", "Tall")

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__("Café Descafeinado", "Tall")

    def cost(self) -> float:
        return 1.05


class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__("Espresso", "Tall")

    def cost(self) -> float:
        return 1.99

 # beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod

# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """
    def __init__(self):
        self.description = "Bebida Desconocida"

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return self.description

    @abstractmethod
    def cost(self) -> float:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida.
        """
        pass

    def set_size(self, size: str):
        """
        Método para establecer el tamaño de la bebida.
        """
        if size not in ['P', 'M', 'G']:
            raise ValueError("Tamaño inválido")
        self.size = size

    def get_size(self) -> str:
        """
        Método para obtener el tamaño de la bebida.
        No implementado en esta versión, pero puede ser extendido.
        """
        return getattr(self, 'size', 'Tamaño no especificado')
    
    def get_size_cost(self) -> float:
        """
        Método para obtener el costo adicional basado en el tamaño.
        No implementado en esta versión, pero puede ser extendido.
        """
        size_costs = {'P': 1, 'M': 1.10, 'G': 1.20}
        return size_costs[self.size] if hasattr(self, 'size') else 1

# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """
    def __init__(self):
        self.description = "Café de la Casa"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """
    def __init__(self):
        self.description = "Café Dark Roast"

    def cost(self) -> float:
        return 0.99

class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """
    def __init__(self):
        self.description = "Café Descafeinado"

    def cost(self) -> float:
        return 1.05

class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """
    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99

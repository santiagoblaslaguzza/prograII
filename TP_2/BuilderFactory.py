from beverages import Espresso, DarkRoast, HouseBlend, Decaf
from condiments import Milk, Mocha, Soy, Whip, Caramel
from collections import Counter

CONDIMENT_MAP = {
    "Milk": Milk,
    "Mocha": Mocha,
    "Soy": Soy,
    "Whip": Whip,
    "Caramel": Caramel,
}

BASE_MAP = {
    "Espresso": Espresso,
    "DarkRoast": DarkRoast,
    "HouseBlend": HouseBlend,
    "Decaf": Decaf,
}

def build_beverage(base: str, size: str = "Mediano", condiments: list[str] = None):
    """
    Crea una bebida con base, tamaño y lista de condimentos.
    """
    if condiments is None:
        condiments = []
    if base not in BASE_MAP:
        raise ValueError(f"Base '{base}' no encontrada.")
    
    beverage = BASE_MAP[base]()         # Crear base
    beverage.set_size(size)             # Asignar tamaño
    
    for cond in condiments:             # Aplicar decoradores
        if cond not in CONDIMENT_MAP:
            raise ValueError(f"Condimento '{cond}' no encontrado.")
        beverage = CONDIMENT_MAP[cond](beverage)
    
    return beverage

# pretty print
def pretty_description(beverage) -> str:
    """
    Convierte descripciones repetidas como 'Mocha, Mocha, Whip'
    en 'Double Mocha, Whip' solo para mostrar.
    """
    desc = beverage.get_description().split(", ")
    counts = Counter(desc)
    parts = []
    for item, count in counts.items():
        if count == 1:
            parts.append(item)
        elif count == 2:
            parts.append(f"Double {item}")
        elif count == 3:
            parts.append(f"Triple {item}")
        else:
            parts.append(f"{count}x {item}")
    return ", ".join(parts)
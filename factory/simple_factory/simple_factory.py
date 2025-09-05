from typing import Type
from .pizza import Pizza, CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza

class SimplePizzaFactory:
    def create_pizza(self, kind: str) -> Pizza:
        k = kind.lower()
        if k == "cheese": return CheesePizza()
        if k == "veggie": return VeggiePizza()
        if k == "clam": return ClamPizza()
        if k == "pepperoni": return PepperoniPizza()
        raise ValueError(f"Tipo inválido: {kind}")

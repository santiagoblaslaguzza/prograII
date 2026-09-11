from abc import ABC, abstractmethod
from .pizza import (
    Pizza,
    NYStyleCheesePizza, ChicagoStyleCheesePizza,
    NYStyleVeggiePizza, ChicagoStyleVeggiePizza,
    NYStylePepperoniPizza, ChicagoStylePepperoniPizza,
    NYStyleClamPizza, ChicagoStyleClamPizza,
)

class PizzaStore(ABC):
    def order_pizza(self, kind: str) -> Pizza:
        pizza = self.create_pizza(kind)
        pizza.prepare(); pizza.bake(); pizza.cut(); pizza.box()
        return pizza
    @abstractmethod
    def create_pizza(self, kind: str) -> Pizza: ...

class NYPizzaStore(PizzaStore):
    def create_pizza(self, kind: str) -> Pizza:
        k = kind.lower()
        if k == "cheese":    return NYStyleCheesePizza()
        if k == "veggie":    return NYStyleVeggiePizza()
        if k == "clam":      return NYStyleClamPizza()
        if k == "pepperoni": return NYStylePepperoniPizza()
        raise ValueError(f"No NY pizza for kind: {kind}")

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, kind: str) -> Pizza:
        k = kind.lower()
        if k == "cheese":    return ChicagoStyleCheesePizza()
        if k == "veggie":    return ChicagoStyleVeggiePizza()
        if k == "clam":      return ChicagoStyleClamPizza()
        if k == "pepperoni": return ChicagoStylePepperoniPizza()
        raise ValueError(f"No Chicago pizza for kind: {kind}")

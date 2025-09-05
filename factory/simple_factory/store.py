from .simple_factory import SimplePizzaFactory
from .pizza import Pizza

class PizzaStore:
    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, kind: str) -> Pizza:
        pizza = self.factory.create_pizza(kind)
        pizza.prepare(); pizza.bake(); pizza.cut(); pizza.box()
        return pizza

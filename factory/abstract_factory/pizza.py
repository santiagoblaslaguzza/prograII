from abc import ABC, abstractmethod
from .ingredients import PizzaIngredientFactory

class Pizza(ABC):
    def __init__(self, name: str, ing_factory: PizzaIngredientFactory):
        self.name=name; self.f=ing_factory
        self.dough=None; self.sauce=None; self.cheese=None; self.clam=None
        self.veggies=None; self.pepperoni=None
    @abstractmethod
    def prepare(self): ...
    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class CheesePizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough=self.f.create_dough(); self.sauce=self.f.create_sauce(); self.cheese=self.f.create_cheese()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese)

class ClamPizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough=self.f.create_dough(); self.sauce=self.f.create_sauce(); self.cheese=self.f.create_cheese(); self.clam=self.f.create_clam()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese, "/", self.clam)

class VeggiePizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough=self.f.create_dough(); self.sauce=self.f.create_sauce(); self.cheese=self.f.create_cheese(); self.veggies=self.f.create_veggies()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese, "/", self.veggies)

class PepperoniPizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough=self.f.create_dough(); self.sauce=self.f.create_sauce(); self.cheese=self.f.create_cheese(); self.pepperoni=self.f.create_pepperoni()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese, "/", self.pepperoni)

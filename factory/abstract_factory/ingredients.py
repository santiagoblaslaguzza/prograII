from abc import ABC, abstractmethod

# Ingredient products
class Dough:    def __init__(self, name): self.name=name;  def __str__(self): return self.name
class Sauce:    def __init__(self, name): self.name=name;  def __str__(self): return self.name
class Cheese:   def __init__(self, name): self.name=name;  def __str__(self): return self.name
class Clams:    def __init__(self, name): self.name=name;  def __str__(self): return self.name

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   return Clams("Fresh Clams")

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:   return Clams("Frozen Clams")

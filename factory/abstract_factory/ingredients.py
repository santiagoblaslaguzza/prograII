from abc import ABC, abstractmethod

# Ingredient products
class Ingredient:
    def __init__(self, name): self.name = name
    def __str__(self): return self.name

class Dough(Ingredient): ...
class Sauce(Ingredient): ...
class Cheese(Ingredient): ...
class Clams(Ingredient): ...
class Veggies(Ingredient): ...
class Pepperoni(Ingredient): ...

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
    @abstractmethod
    def create_veggies(self) -> Veggies: ...
    @abstractmethod
    def create_pepperoni(self) -> Pepperoni: ...

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:        return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:        return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:      return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:         return Clams("Fresh Clams")
    def create_veggies(self) -> Veggies:    return Veggies("Onion, Garlic, Mushroom, Red Pepper")
    def create_pepperoni(self) -> Pepperoni:return Pepperoni("Sliced Pepperoni")

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:        return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:        return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:      return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:         return Clams("Frozen Clams")
    def create_veggies(self) -> Veggies:    return Veggies("Spinach, Black Olives, Eggplant")
    def create_pepperoni(self) -> Pepperoni:return Pepperoni("Chicago-style Pepperoni")

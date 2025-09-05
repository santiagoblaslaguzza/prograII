from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    dough: str = ""
    sauce: str = ""
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for t in self.toppings:
            print("  ", t)

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class CheesePizza(Pizza):
    def __init__(self):
        self.name="Cheese Pizza"; self.dough="Regular"; self.sauce="Marinara"; self.toppings=["Reggiano cheese"]

class VeggiePizza(Pizza):
    def __init__(self):
        self.name="Veggie Pizza"; self.dough="Thin"; self.sauce="Marinara"; self.toppings=["Mushroom","Onion","Red Pepper"]

class ClamPizza(Pizza):
    def __init__(self):
        self.name="Clam Pizza"; self.dough="Thin"; self.sauce="White"; self.toppings=["Fresh Clams","Grated Cheese"]

class PepperoniPizza(Pizza):
    def __init__(self):
        self.name="Pepperoni Pizza"; self.dough="Regular"; self.sauce="Marinara"; self.toppings=["Sliced Pepperoni","Onion","Cheese"]

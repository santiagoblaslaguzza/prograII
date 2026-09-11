from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="NY Style Sauce & Cheese"; self.toppings=["Reggiano cheese"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Cheese"; self.toppings=["Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name="NY Style Veggie"; self.toppings=["Mushroom","Onion","Red Pepper"]

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Veggie"; self.toppings=["Spinach","Black Olives","Eggplant"]
    def cut(self): print("Cutting the pizza into square slices")

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name="NY Style Pepperoni"; self.toppings=["Sliced Pepperoni","Onion","Reggiano cheese"]

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Pepperoni"; self.toppings=["Chicago-style Pepperoni","Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

class NYStyleClamPizza(Pizza):
    def __init__(self):
        self.name="NY Style Clam"; self.toppings=["Fresh Clams","Reggiano cheese"]

class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Clam"; self.toppings=["Frozen Clams","Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

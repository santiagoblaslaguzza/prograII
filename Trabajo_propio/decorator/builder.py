from typing import List, Optional
from beverages import Beverage, Espresso, DarkRoast, HouseBlend, Decaf
from condiments import Milk, Mocha, Soy, Whip, Caramel


class BeverageBuilder:
    BEVERAGES = {
        "espresso": Espresso,
        "darkroast": DarkRoast,
        "houseblend": HouseBlend,
        "decaf": Decaf,
    }

    CONDIMENTS = {
        "milk": Milk,
        "mocha": Mocha,
        "soy": Soy,
        "whip": Whip,
        "caramel": Caramel,
    }

    SIZES = {"Tall", "Grande", "Venti"}

    def __init__(self, beverage: str, size: str) -> Beverage:
        if beverage not in self.BEVERAGES:
            raise ValueError(f"Esa bebida: {beverage} no existe.")
        self.beverage = self.BEVERAGES[beverage]()

        if size not in self.SIZES:
            raise ValueError(f"Ese tamaño: {size} no existe.")
        self.beverage.set_size(size)

    def add_condiment(self, condiment: str):
        if condiment not in self.CONDIMENTS:
            raise ValueError(f"Condimento no reconocido: {condiment}")

        condiment_class = self.CONDIMENTS[condiment]
        self.beverage = condiment_class(self.beverage)
        return self

    def add_condiments(self, condiments: List[str]):
        for c in condiments:
            self.add_condiment(c)

    def build(self) -> Beverage:
        return self.beverage


def build_beverage(base: str, size: str, condiments: Optional[List[str]]) -> Beverage:
    builder = BeverageBuilder(base, size)
    if condiments:
        builder.add_condiments(condiments)

    return builder.build()

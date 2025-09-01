from typing import List, Optional 
from beverages import * #Beverage, Espresso, DarkRoast, HouseBlend, Decaf
from condiments import * #Milk, Mocha, Soy, Whip, Caramel


class BeverageBuilder:

 #   BEVERAGES = {
 #       "espresso": Espresso,
 #       "darkroast": DarkRoast,
 #       "houseblend": HouseBlend,
 #       "decaf": Decaf,
 #    }
    bebidas = Beverage.__subclasses__()
    BEVERAGES = dict(zip([cls.__name__ for cls in bebidas],bebidas))

    """     
    CONDIMENTS = {
        "milk": Milk,
        "mocha": Mocha,
        "soy": Soy,
        "whip": Whip,
        "caramel": Caramel,
    } 
    """
    condimentos = CondimentDecorator.__subclasses__()
    CONDIMENTS = dict(zip([cls.__name__ for cls in condimentos],condimentos))

    SIZES = {"Tall", "Grande", "Venti"}

    def __init__(self, beverage: str, size: Optional[str]) -> Beverage:
       


        if beverage not in self.BEVERAGES:
            raise ValueError(f"Esa bebida: {beverage} no existe.")
        self.beverage = self.BEVERAGES[beverage]()

        if size:
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


def build_beverage(
    base: str, size: Optional[str] = "Tall", condiments: Optional[List[str]] = []
) -> Beverage:
    builder = BeverageBuilder(base, size)
    if condiments:
        builder.add_condiments(condiments)

    return builder.build()

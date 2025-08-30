from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel


def test1():
    # testeo el condimento caramelo Un Espresso simple (1.99), con caramelo (0.20).
    beverage_T1 = Espresso()
    beverage_T1 = Mocha(beverage_T1)  # Envolvemos con el primer Mocha
    print(f"Test 1: {beverage_T1.get_description()} ${beverage_T1.cost():.2f} Size: {beverage_T1.size}")
    if beverage_T1.cost()  == 2.19:
        print("Cálculo correcto de costo")
    else:
        print("Debería costar 2.19")
    print("-----------------")

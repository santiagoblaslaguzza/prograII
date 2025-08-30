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


def test2():
    # testeo en el Espresso simple (1.99), con caramelo (0.20), cambio de tamaño.
    beverage_T2 = Espresso()
    beverage_T2.set_size("Grande")
    beverage_T2 = Mocha(beverage_T2)  # Envolvemos con el primer Mocha
    print(f"Test 2: {beverage_T2.get_description()} ${beverage_T2.cost():.2f} Size: {beverage_T2.size}")
    if beverage_T2.cost()  == 2.19:
        print("Cálculo correcto de costo")
    else:
        print("Debería costar 2.19")
    print("-----------------")


def test3():
    # testeo en el Espresso simple (1.99), con caramelo (0.20), cambio de tamaño se setea mal.
    beverage_T3 = Espresso()
    beverage_T3.set_size("Grde")
    beverage_T3 = Mocha(beverage_T3)  # Envolvemos con el primer Mocha
    print(f"Test 3: {beverage_T3.get_description()} ${beverage_T3.cost():.3f} Size: {beverage_T3.size}")
    if beverage_T3.size  =="Tall":
        print("Tamaño Correcto")
    else:
        print("Debería no haber modificado el default Tall")
    print("-----------------")
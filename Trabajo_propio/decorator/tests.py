from beverages import Espresso, DarkRoast, HouseBlend,Decaf
from condiments import Mocha, Whip, Soy, Caramel
import main

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
    # testeo en el HouseBlend  (0.89), con caramelo (0.20), cambio de tamaño se setea mal.
    beverage_T3 = Espresso()
    beverage_T3.set_size("Grde")
    beverage_T3 = Mocha(beverage_T3)  # Envolvemos con el primer Mocha
    print(f"Test 3: {beverage_T3.get_description()} ${beverage_T3.cost():.3f} Size: {beverage_T3.size}")
    if beverage_T3.size  =="Tall":
        print("Tamaño Correcto")
    else:
        print("Debería no haber modificado el default Tall")
    print("-----------------")

def test4():
    # testeo en el HouseBlend  (0.89), tamaño Tall con soja (0.10).
    beverage_T4 = HouseBlend()
    beverage_T4.set_size("Tall")
    beverage_T4 = Soy(beverage_T4)  # Envolvemos con Soja
    print(f"Test 4: {beverage_T4.get_description()} ${beverage_T4.cost():.2f} Size: {beverage_T4.size}")
    if round(beverage_T4.cost()  == 0.99,2):
        print("Costo Correcto")
    else:
        print("Debería costar 0.99")
    print("-----------------")


def test5():
    # testeo en el HouseBlend  (0.89), tamaño Tall con soja x2(0.10x2).
    beverage_T5 = HouseBlend()
    beverage_T5.set_size("Tall")
    beverage_T5 = Soy(beverage_T5)  # Envolvemos con Soja
    beverage_T5 = Soy(beverage_T5)  # Envolvemos con Soja
    print(f"Test 5: {beverage_T5.get_description()} ${beverage_T5.cost():.2f} Size: {beverage_T5.size}")
    if round(beverage_T5.cost()  == 1.09,2):
        print("Costo Correcto")
    else:
        print("Debería costar 1.09")
    print("-----------------")

def test6():
    # testeo en el HouseBlend  (0.89), tamaño Grande con soja x2(0.15x2).
    beverage_T6 = HouseBlend()
    beverage_T6.set_size("Grande")
    beverage_T6 = Soy(beverage_T6)  # Envolvemos con Soja
    beverage_T6 = Soy(beverage_T6)  # Envolvemos con Soja
    print(f"Test 6: {beverage_T6.get_description()} ${beverage_T6.cost():.2f} Size: {beverage_T6.size}")
    if round(beverage_T6.cost()  == 1.19,2):
        print("Costo Correcto")
    else:
        print("Debería costar 1.19")
    print("-----------------")


def test7():
    # testeo en el HouseBlend  (0.89), tamaño Venti con soja x2(0.20x2).
    beverage_T7 = HouseBlend()
    beverage_T7.set_size("Venti")
    beverage_T7 = Soy(beverage_T7)  # Envolvemos con Soja
    beverage_T7 = Soy(beverage_T7)  # Envolvemos con Soja
    print(f"Test 7: {beverage_T7.get_description()} ${beverage_T7.cost():.2f} Size: {beverage_T7.size}")
    if round(beverage_T7.cost()  == 1.29,2):
        print("Costo Correcto")
    else:
        print("Debería costar 1.29")
    print("-----------------")

def test8():
    # testeo en el Decaf  (1.05), tamaño Venti con soja x2(0.20x2) + crema (0.10)) + caramel (0.2).
    beverage_T8 = Decaf()
    beverage_T8.set_size("Venti")
    beverage_T8 = Soy(beverage_T8)  # Envolvemos con Soja
    beverage_T8 = Soy(beverage_T8)  # Envolvemos con Soja
    beverage_T8 = Whip(beverage_T8)  # Envolvemos con Crema
    beverage_T8 = Caramel(beverage_T8)  # Envolvemos con Caramelo
    print(f"Test 8: {beverage_T8.get_description()} ${beverage_T8.cost():.2f} Size: {beverage_T8.size}")
    if round(beverage_T8.cost()  == 1.75,2):
        print("Costo Correcto")
    else:
        print("Debería costar 1.75")
    print("-----------------")

def test9():
    # testeo en el Espresso simple  (1.99), tamaño Venti no deberia cambiar el importe
    beverage_T9 = Espresso()
    beverage_T9.set_size("Venti")

    print(f"Test 9: {beverage_T9.get_description()} ${beverage_T9.cost():.2f} Size: {beverage_T9.size}")
    if round(beverage_T9.cost()  == 1.99,2):
        print("Costo Correcto")
    else:
        print("Debería costar 1.99")
    print("-----------------")

def test10():
    #testeo builder sin condimentos
    beverage4 = main.build_beverage(DarkRoast, "Venti")
    print(f"Pedido build: {beverage4.get_description()} ${beverage4.cost():.2f}  Size: {beverage4.size}")
    if round(beverage4.cost()  == 0.99,2):
        print("Costo Correcto")
    else:
        print("Debería costar 0.99")
    print("-----------------")


def test11():
    #testeo builder con condimentos
    beverage = main.build_beverage(Decaf, "Venti",[Soy,Soy,Whip,Caramel])
    print(f"Pedido build: {beverage.get_description()} ${beverage.cost():.2f}  Size: {beverage.size}")
    if round(beverage.cost()  == 1.75,2):
        print("Costo Correcto")
    else:
        print("Debería costar 1.75")
    print("-----------------")
    print("-----------------")

def tests():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
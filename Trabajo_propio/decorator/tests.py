from beverages import *#Espresso, DarkRoast, HouseBlend, Decaf
from condiments import *#Mocha, Whip, Soy, Caramel
from builder import build_beverage
from pretty_print import impresion



def test1():
    # Nivel 1 
    # testeo el condimento caramelo Un Espresso simple (1.99), con caramelo (0.20).
    beverage_T1 = Espresso()
    beverage_T1 = Caramel(beverage_T1)  # Envolvemos con el primer Caramelo
    print(
        f"Test 1: {beverage_T1.get_description()} ${beverage_T1.cost():.2f} Size: {beverage_T1.size}"
    )
    if beverage_T1.cost() == 2.19:
        print("Cálculo correcto de costo")
    else:
        print("Debería costar 2.19")
    #print(type(beverage_T1.get_description()))
    print(f"Impresión decorada: {impresion(beverage_T1.get_description())}")  
    print("-----------------")

    # testeo el condimento caramelo Un Espresso simple (1.99), con caramelo (0.20) y Crema (0.10).
    beverage_T1 = Espresso()
    beverage_T1 = Caramel(beverage_T1)  # Envolvemos con el primer Caramel
    beverage_T1 = Whip(beverage_T1)  # Envolvemos con Whip
    beverage_T1 = Whip(beverage_T1)  # Envolvemos con Whip
    beverage_T1 = Whip(beverage_T1)  # Envolvemos con Whip
    beverage_T1 = Whip(beverage_T1)  # Envolvemos con Whip
    print(
        f"Test 1: {beverage_T1.get_description()} ${beverage_T1.cost():.2f} Size: {beverage_T1.size}"
    )
    if round(beverage_T1.cost(),2) == 2.59:
        print("Cálculo correcto de costo")
    else:
        print("Debería costar 2.59")
    #print(beverage_T1.pretty_print())
    print(f"Impresión decorada: {impresion(beverage_T1.get_description())}") 
    print("-----------------")

def test2():
    # testeo en el Espresso simple (1.99), con caramelo (0.20), cambio de tamaño.
    beverage_T2 = Espresso()
    beverage_T2.set_size("Grande")
    beverage_T2 = Mocha(beverage_T2)  # Envolvemos con el primer Mocha
    print(
        f"Test 2: {beverage_T2.get_description()} ${beverage_T2.cost():.2f} Size: {beverage_T2.size}"
    )
    if beverage_T2.cost() == 2.19:
        print("Cálculo correcto de costo")
    else:
        print("Debería costar 2.19")
#    print(f"Impresión decorada: {beverage_T2.pretty_print()}")  
    print("-----------------")


def test3():
    # testeo en el HouseBlend  (0.89), con caramelo (0.20), cambio de tamaño se setea mal.
    try:
        beverage_T3 = Espresso()
        beverage_T3.set_size("Grande")
    except ValueError as e:
        assert str(e) == "Tamaño no disponible"


def test4():
    # testeo en el HouseBlend  (0.89), tamaño Tall con soja (0.10).
    beverage_T4 = HouseBlend()
    beverage_T4.set_size("Tall")
    beverage_T4 = Soy(beverage_T4)  # Envolvemos con Soja
    print(
        f"Test 4: {beverage_T4.get_description()} ${beverage_T4.cost():.2f} Size: {beverage_T4.size}"
    )
    if round(beverage_T4.cost(), 2) == 0.99:
        print("Costo Correcto")
    else:
        print("Debería costar 0.99")
#    print(f"Impresión decorada: {beverage_T4.pretty_print()}")  
    print("-----------------")


def test5():
    # testeo en el HouseBlend  (0.89), tamaño Tall con soja x3(0.10x3).
    beverage_T5 = HouseBlend()
    beverage_T5.set_size("Tall")
    beverage_T5 = Soy(beverage_T5)  # Envolvemos con Soja
    beverage_T5 = Soy(beverage_T5)  # Envolvemos con Soja
    beverage_T5 = Soy(beverage_T5)  # Envolvemos con Soja

    print(
        f"Test 5: {beverage_T5.get_description()} ${beverage_T5.cost():.2f} Size: {beverage_T5.size}"
    )
    if round(beverage_T5.cost(), 2) == 1.19:
        print("Costo Correcto")
    else:
        print("Debería costar 1.19")
#    print(f"Impresión decorada: {beverage_T5.pretty_print()}")  
    print(f"Impresión decorada: {impresion(beverage_T5.get_description())}") 
    print("-----------------")


def test6():
    # testeo en el HouseBlend  (0.89), tamaño Grande con soja x2(0.15x2).
    beverage_T6 = HouseBlend()
    beverage_T6.set_size("Grande")
    beverage_T6 = Soy(beverage_T6)  # Envolvemos con Soja
    beverage_T6 = Soy(beverage_T6)  # Envolvemos con Soja
    print(
        f"Test 6: {beverage_T6.get_description()} ${beverage_T6.cost():.2f} Size: {beverage_T6.size}"
    )
    if round(beverage_T6.cost(), 2) == 1.19:
        print("Costo Correcto")
    else:
        print("Debería costar 1.19")
#    print(f"Impresión decorada: {beverage_T6.pretty_print()}")  
    print(f"Impresión decorada: {impresion(beverage_T6.get_description())}") 
    print("-----------------")


def test7():
    # testeo en el HouseBlend  (0.89), tamaño Venti con soja x2(0.20x2).
    beverage_T7 = HouseBlend()
    beverage_T7.set_size("Venti")
    beverage_T7 = Soy(beverage_T7)  # Envolvemos con Soja
    beverage_T7 = Soy(beverage_T7)  # Envolvemos con Soja
    print(
        f"Test 7: {beverage_T7.get_description()} ${beverage_T7.cost():.2f} Size: {beverage_T7.size}"
    )
    if round(beverage_T7.cost() , 2) == 1.29:
        print("Costo Correcto")
    else:
        print("Debería costar 1.29")
#    print(f"Impresión decorada: {beverage_T7.pretty_print()}")  
    print(f"Impresión decorada: {impresion(beverage_T7.get_description())}") 
    print("-----------------")


def test8():
    # testeo en el Decaf  (1.05), tamaño Venti con soja x2(0.20x2) + crema (0.10)) + caramel (0.2).
    beverage_T8 = Decaf()
    beverage_T8.set_size("Venti")
    beverage_T8 = Soy(beverage_T8)  # Envolvemos con Soja
    beverage_T8 = Soy(beverage_T8)  # Envolvemos con Soja
    beverage_T8 = Whip(beverage_T8)  # Envolvemos con Crema
    beverage_T8 = Caramel(beverage_T8)  # Envolvemos con Caramelo
    print(
        f"Test 8: {beverage_T8.get_description()} ${beverage_T8.cost():.2f} Size: {beverage_T8.size}"
    )
    if round(beverage_T8.cost(), 2) == 1.75:
        print("Costo Correcto")
    else:
        print("Debería costar 1.75")
#    print(f"Impresión decorada: {beverage_T8.pretty_print()}")  
    print(f"Impresión decorada: {impresion(beverage_T8.get_description())}") 
    print("-----------------")


def test9():
    # testeo en el Espresso simple  (1.99), tamaño Venti no deberia cambiar el importe
    beverage_T9 = Espresso()
    beverage_T9.set_size("Venti")

    print(
        f"Test 9: {beverage_T9.get_description()} ${beverage_T9.cost():.2f} Size: {beverage_T9.size}"
    )
    if round(beverage_T9.cost(), 2) == 1.99:
        print("Costo Correcto")
    else:
        print("Debería costar 1.99")
#    print(f"Impresión decorada: {beverage_T9.pretty_print()}")  
    print(f"Impresión decorada: {impresion(beverage_T9.get_description())}") 
    print("-----------------")


def test10():
    # testeo builder sin condimentos
    beverage4 = build_beverage("DarkRoast", )
    print(
        f"Pedido build 10 : {beverage4.get_description()} ${beverage4.cost():.2f}  Size: {beverage4.size}"
    )
    if round(beverage4.cost() , 2)== 0.99:
        print("Costo Correcto")
    else:
        print("Debería costar 0.99")
#    print(f"Impresión decorada: {beverage4.pretty_print()}")  
    print("-----------------")


def test11():
    # testeo builder con condimentos
    beverage = build_beverage("Decaf", "Venti", ["Soy", "Soy", "Whip", "Caramel"])
    print(
        f"Pedido build 11: {beverage.get_description()}      ${beverage.cost():.2f}  Size: {beverage.size}"
    )
    if round(beverage.cost(), 2) == 1.75:
        print("Costo Correcto")
    else:
        print("Debería costar 1.75")
#    print(f"Impresión decorada: {beverage.pretty_print()}")
    print(f"Impresión decorada: {impresion(beverage.get_description())}") 
    print("-----------------")    
    
def test12():
    # testeo builder con assert
    print("test12")
    try:
        beverage = build_beverage("decafEE", "Venti", ["Soy", "Soy", "Whip", "Caramel"])
        print(f"Impresión decorada: {impresion(beverage.get_description())}") 
    
    except ValueError as e:
        print(e)
        assert str(e) == "Esa bebida: decafEE no existe."
    print("-----------------")

def test13():
    # testeo builder con condimentos se verifica que sea instancia de bebida y de condimento
    try:
        beverage = build_beverage("Decaf", "Venti", ["Soy", "Soy","Soy", "Whip", "Caramel"])
        print(beverage.get_description())
        print(f"beverage es instancia de Beverage= {isinstance(beverage,Beverage)}")
        print(f"beverage es instancia de Condimentos= {isinstance(beverage,CondimentDecorator)}")        
    except:
        print("Error test 13")
    print("-----------------")

def test14():
    # testeo builder sin condimentos se verifica que sea instancia de bebida y NO de condimento
    try:
        beverage = build_beverage("Decaf", "Venti")
        print(beverage.get_description())
        print(f"beverage es instancia de Beverage= {isinstance(beverage,Beverage)}")
        print(f"beverage es instancia de Condimentos= {isinstance(beverage,CondimentDecorator)}")        
    except:
        print("Error test 14")
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
    test12()    
    test13()
    test14()

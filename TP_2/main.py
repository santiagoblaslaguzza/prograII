# main.py
# Script principal para probar el patrón Decorator.

from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel, Milk
from BuilderFactory import build_beverage, pretty_description

def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} ${beverage1.cost():.2f}")

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)  # Envolvemos con el primer Mocha
    beverage2 = Mocha(beverage2)  # Envolvemos con el segundo Mocha
    beverage2 = Whip(beverage2)   # Envolvemos con Crema
    print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")

    # Pedido 4: Un Espresso con Macha y Caramel
    beverage4 = Espresso() # 1.99
    beverage4 = Mocha(beverage4) # 0.2
    beverage4 = Caramel(beverage4) # 0.2
    print(f"Pedido 4: {beverage4.get_description()} ${beverage4.cost():.2f}")

    # Pedido 5: Un DarkRoast con doble Caramel y Soja
    beverage5 = DarkRoast() # 0.99
    beverage5 = Caramel(beverage5) # 0.2
    beverage5 = Caramel(beverage5) # 0.2
    beverage5 = Soy(beverage5) # 0.15
    print(f"Pedido 5: {beverage5.get_description()} ${beverage5.cost():.2f}")

    # Pedido 6: Un HouseBlend con Leche, Mocha, Caramel y Triple Crema
    beverage6 = HouseBlend() # 0.89
    beverage6 = Milk(beverage6) # 0.1
    beverage6 = Mocha(beverage6) # 0.2
    beverage6 = Caramel(beverage6) # 0.2
    beverage6 = Whip(beverage6) # 0.1
    beverage6 = Whip(beverage6) # 0.1
    beverage6 = Whip(beverage6) # 0.1
    print(f"Pedido 6: {beverage6.get_description()} ${beverage6.cost():.2f}")


    # Pedido 7: Un DarkRoast tamaño Grande con Soja, Mocha y Crema
    beverage7 = DarkRoast() # 0.99
    beverage7.set_size('G') # tamaño Grande
    beverage7 = Soy(beverage7) # 0.15 * 1.20 = 0.18
    beverage7 = Mocha(beverage7) # 0.2
    beverage7 = Whip(beverage7) # 0.1
    print(f"Pedido 7: {beverage7.get_description()} ${beverage7.cost():.2f}")

    # Pedido 8: Tamaño Mediano DarkRoast con Soja y Crema
    beverage8 = DarkRoast() # 0.99
    #beverage8.set_size('P') # tamaño Mediano
    beverage8 = Soy(beverage8) # 0.15 * 1.10 = 0.165
    beverage8 = Whip(beverage8) # 0.1
    beverage8 = Mocha(beverage8) # 0.2
    print(f"Pedido 8: {beverage8.get_description()} ${beverage8.cost():.2f}")   

    # pedido 9: Tamaño Pequeño HouseBlend con Leche y Caramel
    beverage9 = HouseBlend() # 0.89
    beverage9.set_size('P') # tamaño Pequeño
    beverage9 = Milk(beverage9) # 0.1
    beverage9 = Caramel(beverage9) # 0.2
    beverage9 = Soy(beverage9) # 0.15 * 1 = 0.15
    print(f"Pedido 9: {beverage9.get_description()} ${beverage9.cost():.2f}")


    # Pedido 10: Usando el BuilderFactory para crear un DarkRoast tamaño Grande con Soja, Mocha y Crema
    beverage10 = build_beverage("DarkRoast", size="G", condiments=["Soy", "Mocha", "Whip"])
    print(f"Pedido 10: {beverage10.get_description()} ${beverage10.cost():.2f}")

    # Pedido 11: Usando el BuilderFactory para crear un HouseBlend tamaño Pequeño con Leche y Caramel
    beverage11 = build_beverage("HouseBlend", size="P", condiments=["Milk", "Caramel", "Soy", "Caramel"])
    print(f"Pedido 11: {pretty_description(beverage11)} ${beverage11.cost():.2f}")

    # Pedido 12: usando el builderfactory para crear houseblend tamaño mediano con soja y crema
    beverage12 = build_beverage("HouseBlend", size="M", condiments=["Soy", "Whip"])
    print(f"Pedido 12: {pretty_description(beverage12)} ${beverage12.cost():.2f}")

    # Pedido 13
    beverage13 = build_beverage("Espresso", "G", ["Mocha", "Mocha", "Caramel"])
    print(f"Pedido 13: {pretty_description(beverage13)} ${beverage13.cost():.2f}")
    
if __name__ == "__main__":
    main()
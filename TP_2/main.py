# main.py
# Script principal para probar el patrón Decorator.

from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel, Milk

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



if __name__ == "__main__":
    main()
# main.py
# Script principal para probar el patrón Decorator.

from beverages import * # Espresso, DarkRoast, HouseBlend, Decaf
from condiments import * # Mocha, Whip, Soy, Caramel
import tests
import pretty_print
from builder import build_beverage


def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    beverage1 = build_beverage("Espresso")
    print(f"Pedido 1: {beverage1.get_description()} ${beverage1.cost():.2f}")

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = build_beverage("DarkRoast", condiments=["Mocha", "Mocha", "Whip"])
    print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = build_beverage(
        "HouseBlend", size="Grande", condiments=["Soy", "Mocha", "Whip"]
    )
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")

    # Pedido 4: Un Decaf con Soja y Mocha.
    beverage4 = build_beverage("Decaf", "Grande", ["Soy", "Mocha"])
    print(f"Pedido 4: {beverage4.get_description()}    ${beverage4.cost():.2f}")

    tests.tests()



if __name__ == "__main__":
    main()

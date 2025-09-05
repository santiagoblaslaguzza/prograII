# Trabajo Práctico: Patrones de Diseño Factory

## 🎯 Introducción y Objetivos

¡Bienvenido/a al trabajo práctico sobre Patrones de Fábrica\! En este ejercicio, aplicarás los conceptos de **Simple Factory**, **Factory Method** y **Abstract Factory** para resolver un problema de acoplamiento en el código de una pizzería en expansión.

El objetivo es que, al finalizar, puedas:

  * **Identificar** los problemas de mantenimiento y rigidez causados por la instanciación directa de objetos.
  * **Aplicar** los patrones de fábrica para desacoplar el código cliente de las clases concretas.
  * **Comprender** las diferencias, ventajas y desventajas entre Simple Factory, Factory Method y Abstract Factory.
  * **Extender** un diseño existente que utiliza estos patrones, respetando principios como el **Open-Closed Principle (OCP)** y el **Dependency Inversion Principle (DIP)**.
  * **Validar** el comportamiento del diseño a través de pruebas unitarias.

-----

## 📖 Contexto del Problema: La Pizzería de Objectville

El código de este repositorio simula el sistema de `PizzaStore` , una pizzería que necesita gestionar diferentes tipos y estilos de pizza (por ejemplo, estilo Nueva York vs. estilo Chicago). A medida que el negocio crece, el código original que usaba `if/else` para crear cada tipo de pizza se vuelve insostenible.

Tu tarea será explorar y extender las soluciones implementadas, que utilizan patrones de fábrica para hacer el sistema más flexible y mantenible.

-----

## 📂 Estructura del Repositorio

El código está organizado en módulos que representan la evolución del diseño:

  * `factory/simple_factory`: Una implementación básica que encapsula la creación de pizzas en una clase `SimplePizzaFactory`[cite: 2033]. Aunque no es un patrón GoF formal, es un excelente punto de partida.
  * `factory/factory_method`: Una evolución donde la responsabilidad de la creación se delega a subclases (`NYPizzaStore`, `ChicagoPizzaStore`) a través de un "método fábrica" abstracto.
  * `factory/abstract_factory`: La solución más avanzada, que gestiona la creación de **familias de objetos relacionados** (ingredientes) para garantizar la consistencia regional.

-----

## 🚀 Consigna del Trabajo Práctico

### Paso 0: Exploración Inicial

Antes de escribir código, familiarízate con el estado final del proyecto. Ejecuta cada una de las implementaciones para ver cómo funcionan.

```bash
# Ejecuta la versión con Simple Factory
python -m factory.simple_factory.main

# Ejecuta la versión con Factory Method
python -m factory.factory_method.main

# Ejecuta la versión con Abstract Factory
python -m factory.abstract_factory.main
```

**Analiza la salida de cada comando.** Nota las diferencias en la preparación y los ingredientes entre las pizzas de Nueva York y Chicago en la versión final (`abstract_factory`).

### Paso 1: Extender el Patrón Factory Method

La pizzería quiere ampliar su menú. Tu primera tarea es agregar las variedades `VeggiePizza` y `PepperoniPizza` al sistema que usa **Factory Method**.

1.  **Crea las clases de producto concretas:**

      * En `factory/factory_method/pizzas.py`, crea las clases `NYStyleVeggiePizza`, `NYStylePepperoniPizza`, `ChicagoStyleVeggiePizza` y `ChicagoStylePepperoniPizza`.
      * Inspírate en las clases `...CheesePizza` existentes para definir sus ingredientes (masa, salsa, toppings).

2.  **Actualiza los Concrete Creators:**

      * En `factory/factory_method/stores.py`, modifica los métodos `create_pizza` de `NYPizzaStore` y `ChicagoPizzaStore` para que puedan instanciar las nuevas variedades de pizza cuando se les pasa el `kind` "veggie" o "pepperoni".

3.  **Verifica tu implementación:**

      * Modifica `factory/factory_method/main.py` para ordenar las nuevas pizzas y comprueba que se crean correctamente.

### Paso 2: Extender el Patrón Abstract Factory

Ahora, harás lo mismo pero en la versión más compleja, que utiliza **Abstract Factory** para gestionar los ingredientes. El objetivo es asegurar que las nuevas pizzas también usen ingredientes consistentes con su región.

1.  **Define los nuevos productos de ingredientes:**

      * En `factory/abstract_factory/ingredients.py`, crea las clases para los nuevos ingredientes que necesitarás, como `Veggies` y `Pepperoni` (puedes crear clases abstractas y luego concretas como `Onion`, `Mushroom`, `SlicedPepperoni`, etc.).

2.  **Actualiza la interfaz de la fábrica abstracta:**

      * En el mismo archivo, agrega nuevos métodos abstractos a `PizzaIngredientFactory` para crear los nuevos tipos de ingredientes (ej: `create_veggies()` y `create_pepperoni()`).

3.  **Actualiza las fábricas concretas:**

      * Implementa los nuevos métodos en `NYPizzaIngredientFactory` y `ChicagoPizzaIngredientFactory`, devolviendo las familias de ingredientes correctas para cada región.

4.  **Crea las nuevas clases de Pizza:**

      * En `factory/abstract_factory/pizzas.py`, crea las clases `VeggiePizza` y `PepperoniPizza`.
      * **Punto clave:** Su método `prepare()` debe usar la `ingredient_factory` que reciben en el constructor para obtener los ingredientes, de la misma forma que lo hacen `CheesePizza` y `ClamPizza`.

5.  **Actualiza los `PizzaStore`:**

      * Finalmente, en `factory/abstract_factory/store.py`, modifica `NYPizzaStore` y `ChicagoPizzaStore` para que puedan crear instancias de `VeggiePizza` y `PepperoniPizza`.

### Paso 3: Pruebas Unitarias

La calidad es clave en Objectville. Debes escribir pruebas para asegurar que el sistema funciona como se espera.

1.  **Crea un archivo de pruebas:** Por ejemplo, `factory/abstract_factory/test_pizzas.py`.

2.  **Escribe entre 3 y 5 pruebas** que verifiquen los siguientes escenarios en la implementación de **Abstract Factory**:

      * Que `NYPizzaStore` efectivamente crea una pizza de tipo `NYStyle...`.
      * Que `ChicagoPizzaStore` crea una pizza de tipo `ChicagoStyle...`.
      * Que una pizza de queso de NY (`CheesePizza` creada por `NYPizzaStore`) contiene los ingredientes correctos de NY (ej: `Thin Crust Dough`).
      * Que una pizza de almejas de Chicago (`ClamPizza` creada por `ChicagoPizzaStore`) contiene los ingredientes correctos de Chicago (ej: `Frozen Clams`).

    **Pista para las pruebas:** Puedes instanciar una tienda, ordenar una pizza y luego usar `isinstance` para verificar el tipo de los ingredientes.

    ```python
    # Ejemplo de esqueleto de prueba con pytest
    from .store import NYPizzaStore
    from .ingredients import ThinCrustDough

    def test_ny_cheese_pizza_has_correct_dough():
        # Arrange
        store = NYPizzaStore()
        # Act
        pizza = store.order_pizza("cheese")
        # Assert
        assert isinstance(pizza.dough, ThinCrustDough)
    ```

-----

## 📦 Formato de Entrega

1.  Realiza un **fork** de este repositorio.
2.  Trabaja en tu fork, haciendo commits a medida que completas cada paso.
3.  En tu propio `README.md`, escribe una breve sección (`## Decisiones de Diseño`) explicando las decisiones que tomaste y cualquier desafío que encontraste.
4.  La entrega final será el enlace a tu repositorio de GitHub.

**¡Mucha suerte y a codificar\!**

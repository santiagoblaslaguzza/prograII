# INFORME TP DECORADOR GRUPO 5 -- Starbuzz Coffee

El programa ya armado incluía la siguiente salida
```
Bienvenido a Starbuzz Coffee!
--- Preparando pedidos ---
   Pedido 1: Espresso $1.99
   Pedido 2: Café Dark Roast, Mocha, Mocha, Crema $1.49
   Pedido 3: Café de la Casa, Soja, Mocha, Crema $1.34
```

---
  
##  Trabajo Práctico (TP) — Consignas y entregables
  
   Se trabaja en repositorio https://github.com/Gianni2025/prograII
   Dentro de la carpeta Tabajo_propio/decorador

### Nivel 1 — Calentamiento     
1. **Nuevo condimento**: implementar `Caramel` (Caramelo) con un costo fijo (p. ej., `$0.20`).  
- Actualizar `get_description()` y `cost()` como en `Mocha`.  
- Demostrar en `main.py` un pedido con Caramelo.

   En condiments.py se sumo el "Condimento Concreto" Caramel
   class Caramel(CondimentDecorator):
   """
               Decorador para añadir Caramelo a una bebida.
               """
   def get_description(self) -> str:
   return self._beverage.get_description() + ", Caramelo"

   def cost(self) -> float:
   return self._beverage.cost() + 0.20

   Se agregó un archivo tests.py para agregar los testeos de las nuevas implementaciones, el Test1 muestra una expreso + caramel  y un expreso + caramel + whip, para verificar que tanto su uso solo como en combinación con otros condimentos es incorporado correctamente


2. **Doble/Triple**: crear bebidas con **doble** y **triple** condimento (p. ej., *Double Mocha*). Animarse a encadenar muchas capas; confirmar que los totales se calculan bien.

   En realidadel pedido 2 ya incluído en el main.py muestra un doble mocha.
   En varios de los test incluídos en tests.py se usa multiplicidad de un condimento.
   Solo a modo de ejemplo:
      En el test 1 se usa multiplicidad de Crema
      En el test5 del archivos tests.py se muestra un Café de la casa condimentado con soja x3.


### Nivel 2 — Tamaños (**Tall/Grande/Venti**) y precios dependientes del tamaño
1. Agregar a `Beverage` las operaciones `set_size(size)` y `get_size()`. 

   Se agregaron los métodos. Se considera que si hay un ingreso erróneo del tamaño se toma el default 'Tall", y en la clase abstracta de 'CondimentDecorator' se agregó en el init "self.size = beverage.get_size()" para que al ir decorando la bebida mantenga el estado de tamaño.
   En los tests 2 y 3 se verifica que aún con condimentos reconoce el tamaño seteado

      def set_size(self, size) -> str:
         sizes= ["Tall", "Grande", "Venti"]
         if size in sizes:
               self.size = size
         else:
               print("Tamaño ingresado erróneo, se asume Tall")
               
      def get_size(self) -> str:
         return self.size

      class CondimentDecorator(Beverage, ABC):
      """
      Clase base para los decoradores de condimentos.
      Hereda de Beverage para tener el mismo tipo.
      Mantiene una referencia a la bebida que está envolviendo.
      """
      def __init__(self, beverage: Beverage):
         self._beverage = beverage
         self.size = beverage.get_size()
      

2. Hacer que **al menos** `Soy` cobre según tamaño (p. ej., Tall 0.10, Grande 0.15, Venti 0.20) y leer el `size` del componente envuelto.  

   Se modifica el metodo cost() del decorador Soy. 

   def cost(self) -> float:
      costo = [0.10, 0.15 , 0.20]
      if self.size == "Tall":
            return self._beverage.cost() + costo[0]
      elif self.size == "Grande":
            return self._beverage.cost() + costo[1]
      else:
            return self._beverage.cost() + costo[2]      


3. Validar con 2–3 ejemplos reales: *HouseBlend Venti + Soy*, etc.  
   > Pista: los decoradores deben **propagar** o **consultar** el tamaño del beverage envuelto; no dupliques estado.

   Se realizaron tests con distintos cafés/tamaños decorados con soja solo, con multiplicidad y en combinación con otros condimentos, verificando el correcto cálculo del precio, tests 4 a 9


### Nivel 3 — Usabilidad y pruebas
1. **Builder/Factory simple (opcional)**: para no escribir a mano todas las “envolturas”, crear una función tipo `build_beverage(base, size, condiments)` que devuelva el objeto ya decorado.  

   Se generó el archivo builder.py, toma como opcionales tamaño (el default sigue siendo Tall) y condimentos.
   Esta clase toma en forma automática las clases concretas de bebidas y condimentos

2. **Pretty print (opcional)**: un decorador “de presentación” que transforme `"Mocha, Mocha, Whip"` en `"Double Mocha, Whip"` **solo a nivel de texto** (no cambies la lógica de `cost()`).


   Se generó método pretty_print en beverages y condiments, 
   en los test se agregó la impresión decorada para evaluar la funcionalidad


3. **Testing**: escribir tests (con `pytest` o asserts) para validar costos y descripciones de 3–5 combos (incluyendo **dobles** y **tamaños**).



### Entregables
- Código fuente actualizado (`beverages.py`, `condiments.py`, `main.py`, y/o `builder.py` si lo agregás).  
   https://github.com/Gianni2025/prograII/tree/builder-toma-las-clases-automaticamente/Trabajo_propio/decorator

- Casos de prueba (mínimo 3).  
   En main y tests.py

- Un **breve informe** (puede ser en el README) explicando decisiones de diseño (cómo propagaste `size`, cómo probaste totales, etc.).
   Informe TP Decorador.md en mismo repositorio
---

## 5) Buenas prácticas y “pitfalls”

- **Programa contra la abstracción** (`Beverage`), no contra tipos concretos: si tu cliente chequea el tipo concreto de la bebida (p. ej., `isinstance(..., HouseBlend)`), al decorar se puede **romper** esa lógica. Evitalo. fileciteturn3file1  
- **OCP**: para añadir un **nuevo condimento**, creá un **nuevo decorador**; **no** modifiques `Beverage` ni las bebidas existentes. fileciteturn3file1  
- **Pequeñas clases**: Decorator tiende a generar **muchas clases pequeñas**; documentá y organizá bien para mantener la comprensión. fileciteturn3file1

---

## 6) Extensión sugerida: Decorator en I/O (paralelo con Java)

El capítulo muestra cómo el paquete **java.io** usa Decorator (`InputStream` + `FilterInputStream` + `BufferedInputStream`, `ZipInputStream`, etc.). Como extensión, implementá un **wrapper** en Python para un “stream” de texto que **convierte a minúsculas** al leer, análogo a `LowerCaseInputStream`. fileciteturn3file1

---

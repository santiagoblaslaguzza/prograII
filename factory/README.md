# Patrones de Fábrica — guía de la clase

Este código acompaña la clase teórica sobre los patrones de creación
**Simple Factory**, **Factory Method** y **Abstract Factory**, usando como
excusa una pizzería que va creciendo. Cada carpeta es un paso en esa
evolución: mismo dominio (pizzas), problema cada vez más grande, y una
solución de diseño distinta para cada uno.

Las tres implementaciones terminan soportando las mismas 4 variedades de
pizza — `cheese`, `veggie`, `clam`, `pepperoni` — para que se pueda comparar
manzanas con manzanas entre un patrón y otro.

---

## 1. El problema sin patrón: `if/else` por todos lados

Antes de tener una fábrica, `PizzaStore.order_pizza()` tendría un bloque
`if/else` (o `match`) que instancia directamente `new CheesePizza()`,
`new VeggiePizza()`, etc. Cada vez que se agrega una pizza hay que tocar esa
función, y si hay más de un `PizzaStore` (una tienda por ciudad, por
ejemplo), hay que repetir el mismo `if/else` en cada una. El código cliente
queda acoplado a las clases concretas de producto.

Este paso no tiene carpeta propia — es el "antes" contra el que se comparan
los patrones siguientes.

## 2. Simple Factory → [`simple_factory/`](simple_factory/)

No es un patrón GoF formal, pero es el primer paso natural: sacar el
`if/else` de creación y ponerlo en un único lugar, una clase
`SimplePizzaFactory` que sabe construir cualquier pizza a partir de un
`kind`.

- [`pizza.py`](simple_factory/pizza.py) — clases de producto (`CheesePizza`,
  `VeggiePizza`, `ClamPizza`, `PepperoniPizza`).
- [`simple_factory.py`](simple_factory/simple_factory.py) — el `if/else`
  vive acá, y solo acá.
- [`store.py`](simple_factory/store.py) — `PizzaStore` ya no sabe instanciar
  pizzas, solo le pide una a la factory y ejecuta el flujo
  (`prepare/bake/cut/box`).

El `if/else` no desaparece, se **centraliza**. Sigue habiendo un lugar que
hay que tocar para agregar una pizza nueva, pero ya no está duplicado en
cada punto del código que crea pizzas.

## 3. El problema de las franquicias: NY vs Chicago

Ahora la pizzería abre sucursales en Nueva York y Chicago, y cada una
prepara las pizzas a su manera (distinta masa, distinto corte). Una sola
`SimplePizzaFactory` ya no alcanza: necesitamos variar **el algoritmo de
creación completo** según la sucursal, no solo qué clase se instancia. Ahí
es donde Simple Factory se queda corto y entra Factory Method.

## 4. Factory Method → [`factory_method/`](factory_method/)

La idea: en vez de una factory externa, la creación se convierte en un
método de la propia clase que va a usar el producto, y se delega a las
subclases decidir qué implementación concreta instanciar.

Mapeo con el diagrama clásico Product / Creator / ConcreteProduct /
ConcreteCreator:

| Rol del patrón      | En este código                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **Product**          | `Pizza` (clase abstracta) — [`pizza.py`](factory_method/pizza.py)               |
| **ConcreteProduct**  | `NYStyleCheesePizza`, `ChicagoStyleVeggiePizza`, etc. — mismo archivo           |
| **Creator**          | `PizzaStore` (abstracta, define `order_pizza` y el método fábrica `create_pizza`) — [`store.py`](factory_method/store.py) |
| **ConcreteCreator**  | `NYPizzaStore`, `ChicagoPizzaStore` — mismo archivo                             |

`PizzaStore.order_pizza()` es un método concreto que no sabe qué pizza va a
crear: llama a `self.create_pizza(kind)`, que es abstracto. Cada subclase
(`NYPizzaStore`, `ChicagoPizzaStore`) decide qué `ConcreteProduct`
instanciar. El algoritmo general (`prepare → bake → cut → box`) vive una
sola vez en la clase base; lo que varía por región es únicamente la
creación.

## 5. Principio de Inversión de Dependencias (DIP)

Con Factory Method, `PizzaStore` (módulo de alto nivel) ya no depende de
`NYStyleCheesePizza` (detalle de bajo nivel) — depende de la abstracción
`Pizza`. Son las subclases concretas las que dependen de las clases
concretas de producto, no la clase base. Esto es DIP en acción: los módulos
de alto nivel no deberían depender de módulos de bajo nivel, ambos deberían
depender de abstracciones.

Pero todavía queda una dependencia concreta escondida: cada `ConcreteProduct`
(`NYStyleCheesePizza`, etc.) tiene sus ingredientes *hardcodeados* adentro
(`"Reggiano cheese"`, `"Marinara"`...). Si dos regiones necesitan compartir
la garantía de que los ingredientes son consistentes entre sí (la masa, la
salsa y el queso de NY siempre van juntos, nunca mezclados con los de
Chicago), hace falta un nivel más de abstracción: una fábrica de
**familias** de ingredientes.

## 6. Abstract Factory → [`abstract_factory/`](abstract_factory/)

Acá la creación se divide en dos jerarquías que colaboran:

- Una fábrica de **ingredientes** por región, que garantiza que todos los
  ingredientes que devuelve son consistentes entre sí (familia de
  productos relacionados).
- Las clases de **pizza**, que ya no hardcodean ingredientes: se los piden a
  la fábrica que reciben por constructor.

| Archivo | Qué define |
|---|---|
| [`ingredients.py`](abstract_factory/ingredients.py) | `PizzaIngredientFactory` (Abstract Factory) con un método `create_x()` por tipo de ingrediente (`dough`, `sauce`, `cheese`, `clam`, `veggies`, `pepperoni`); `NYPizzaIngredientFactory` y `ChicagoPizzaIngredientFactory` (Concrete Factories) devuelven la familia completa para su región. |
| [`pizza.py`](abstract_factory/pizza.py) | `Pizza` recibe una `PizzaIngredientFactory` en el constructor (`self.f`). `CheesePizza`, `ClamPizza`, `VeggiePizza`, `PepperoniPizza` arman su `prepare()` pidiéndole los ingredientes a `self.f`, sin saber si es la fábrica de NY o de Chicago. |
| [`store.py`](abstract_factory/store.py) | `NYPizzaStore` y `ChicagoPizzaStore` (siguen siendo Factory Method para el *tipo* de pizza) instancian la `PizzaIngredientFactory` correcta y se la pasan a cada pizza. |

Los dos patrones conviven: **Factory Method** decide *qué tipo* de pizza se
crea (cheese/veggie/clam/pepperoni), **Abstract Factory** decide *con qué
familia de ingredientes* se prepara (NY o Chicago). Es el mismo problema de
consistencia regional del punto 3, resuelto ahora también a nivel de
ingredientes, no solo de estilo de pizza.

---

## Cómo correr cada demo

Desde la raíz del repositorio:

```bash
python3 -m factory.simple_factory.main
python3 -m factory.factory_method.main
python3 -m factory.abstract_factory.main
```

Cada una imprime el flujo completo (`prepare → bake → cut → box`) para
varias pizzas, para poder comparar en vivo cómo cambia el resultado según
el patrón y la región.

## Tests

```bash
pytest factory/tests/test_smoke.py
```

Es solo un smoke test de imports — confirma que las tres implementaciones
cargan sin errores. Sirve como red mínima si se modifica el código en vivo
durante la clase.

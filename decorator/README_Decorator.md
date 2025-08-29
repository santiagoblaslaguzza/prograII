
# Clase 2 — Patrón **Decorator** (Starbuzz Coffee)

Este README acompaña a la **Clase 2** y al código de ejemplo en Python (`beverages.py`, `condiments.py`, `main.py`). El objetivo es **aprender y practicar** el patrón **Decorator** tal como se presenta en *Head First Design Patterns* (Cap. 3), y conectar los conceptos con un ejercicio guiado y extensiones.

> Idea central: **extender comportamiento por composición** (envoltura) sin tocar el código probado de las clases base (cumplir **Open–Closed Principle**). Decoramos objetos en **tiempo de ejecución** agregando responsabilidades (p. ej., condimentos) de manera flexible. fileciteturn3file1

---

## 1) Contexto y vínculo con la clase

En la clase vimos que modelar todas las combinaciones de **bebidas + condimentos** con **herencia** lleva a una **explosión de clases** y a diseños rígidos. Decorator propone **envolver** un objeto base con uno o más **decoradores** que comparten su tipo y **delegan** la mayor parte del trabajo al objeto envuelto, **añadiendo** su aporte antes/después. fileciteturn3file0

**Principio Open–Closed (OCP):** *clases abiertas a extensión y cerradas a modificación*. Decorator es un patrón que nos permite **extender** sin **modificar** código existente. fileciteturn3file1

---

## 2) Estructura del repo / archivos

- `beverages.py` — **Component** abstracto `Beverage` y **ConcreteComponents**: `Espresso`, `DarkRoast`, `HouseBlend`, `Decaf`.  
- `condiments.py` — **Decorator** abstracto `CondimentDecorator` y **ConcreteDecorators**: `Milk`, `Mocha`, `Soy`, `Whip`.  
- `main.py` — Script de ejemplo (**Starbuzz**), donde se arman pedidos decorando bebidas y se imprime **descripción + costo**.

**Cómo ejecutarlo:**

```bash
python main.py
```

Deberías ver salidas del estilo (los totales dependen de los precios fijados en `condiments.py`):

```
Bienvenido a Starbuzz Coffee!
--- Preparando pedidos ---
Pedido 1: Espresso $1.99
Pedido 2: Café Dark Roast, Mocha, Mocha, Crema $1.49
Pedido 3: Café de la Casa, Soja, Mocha, Crema $1.34
```

---

## 3) Diseño (qué está pasando)

- **Component** (`Beverage`): define la interfaz común (`get_description()`, `cost()`).
- **ConcreteComponent** (p. ej., `Espresso`, `DarkRoast`, …): implementan costo base y descripción.
- **Decorator** (`CondimentDecorator`): hereda de `Beverage` para **igualar el tipo** y **envolver** (`HAS-A`) una `Beverage` interna.  
- **ConcreteDecorator** (`Milk`, `Mocha`, `Soy`, `Whip`): **delegan** al componente interno y **suman** su propia responsabilidad: costo extra y/o etiqueta en descripción.

### Delegación en cadena (cómo se suman los costos)
Si pedimos **DarkRoast + Mocha + Mocha + Whip**, cuando invocamos `cost()` en el **decorador más externo** (*Whip*), este **delegará** hacia adentro y cada decorador sumará su extra, hasta llegar a la bebida base. Resultado final = **costo base + extras**. fileciteturn3file1

---

## 4) Trabajo Práctico (TP) — Consignas y entregables

> Recomendación: resolver en **pequeños commits**, con **pruebas** por cada consigna.

### Nivel 1 — Calentamiento
1. **Nuevo condimento**: implementar `Caramel` (Caramelo) con un costo fijo (p. ej., `$0.20`).  
   - Actualizar `get_description()` y `cost()` como en `Mocha`.  
   - Demostrar en `main.py` un pedido con Caramelo.
2. **Doble/Triple**: crear bebidas con **doble** y **triple** condimento (p. ej., *Double Mocha*). Animarse a encadenar muchas capas; confirmar que los totales se calculan bien.

### Nivel 2 — Tamaños (**Tall/Grande/Venti**) y precios dependientes del tamaño
1. Agregar a `Beverage` las operaciones `set_size(size)` y `get_size()`.  
2. Hacer que **al menos** `Soy` cobre según tamaño (p. ej., Tall 0.10, Grande 0.15, Venti 0.20) y leer el `size` del componente envuelto.  
3. Validar con 2–3 ejemplos reales: *HouseBlend Venti + Soy*, etc.  
   > Pista: los decoradores deben **propagar** o **consultar** el tamaño del beverage envuelto; no dupliques estado. fileciteturn3file1

### Nivel 3 — Usabilidad y pruebas
1. **Builder/Factory simple (opcional)**: para no escribir a mano todas las “envolturas”, crear una función tipo `build_beverage(base, size, condiments)` que devuelva el objeto ya decorado.  
2. **Pretty print (opcional)**: un decorador “de presentación” que transforme `"Mocha, Mocha, Whip"` en `"Double Mocha, Whip"` **solo a nivel de texto** (no cambies la lógica de `cost()`).
3. **Testing**: escribir tests (con `pytest` o asserts) para validar costos y descripciones de 3–5 combos (incluyendo **dobles** y **tamaños**).

### Entregables
- Código fuente actualizado (`beverages.py`, `condiments.py`, `main.py`, y/o `builder.py` si lo agregás).  
- Casos de prueba (mínimo 3).  
- Un **breve informe** (puede ser en el README) explicando decisiones de diseño (cómo propagaste `size`, cómo probaste totales, etc.).

---

## 5) Buenas prácticas y “pitfalls”

- **Programa contra la abstracción** (`Beverage`), no contra tipos concretos: si tu cliente chequea el tipo concreto de la bebida (p. ej., `isinstance(..., HouseBlend)`), al decorar se puede **romper** esa lógica. Evitalo. fileciteturn3file1  
- **OCP**: para añadir un **nuevo condimento**, creá un **nuevo decorador**; **no** modifiques `Beverage` ni las bebidas existentes. fileciteturn3file1  
- **Pequeñas clases**: Decorator tiende a generar **muchas clases pequeñas**; documentá y organizá bien para mantener la comprensión. fileciteturn3file1

---

## 6) Extensión sugerida: Decorator en I/O (paralelo con Java)

El capítulo muestra cómo el paquete **java.io** usa Decorator (`InputStream` + `FilterInputStream` + `BufferedInputStream`, `ZipInputStream`, etc.). Como extensión, implementá un **wrapper** en Python para un “stream” de texto que **convierte a minúsculas** al leer, análogo a `LowerCaseInputStream`. fileciteturn3file1

---

## 7) Criterios de evaluación

- Correctitud funcional (cálculo de `cost()` y composición de `get_description()`).
- Uso adecuado de **composición + delegación** (no duplicar lógica en cada decorador).
- Cumplimiento de **OCP**: agregar condimentos sin modificar clases existentes.
- Calidad del código y **pruebas** (claridad, casos relevantes, reproducibilidad).
- Extensiones (tamaños, builder, pretty print, I/O decorator) — **bonus**.

---

## Referencias
- *Head First Design Patterns*, Capítulo **3 — The Decorator Pattern** (Starbuzz, OCP, delegación, tamaños, Java I/O). fileciteturn3file0 fileciteturn3file1

---

> **Tip docente:** al finalizar, pedí a cada grupo que muestre un *diagrama simple* (Component/Decorator) y que justifique brevemente cómo su solución **satisface OCP** y dónde **no** lo aplicaron (para discutir trade-offs realistas).

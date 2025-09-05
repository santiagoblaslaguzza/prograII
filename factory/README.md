# Clase 3 — Patrones de Fábrica (Python)

Implementaciones mínimas y didácticas basadas en el caso **Pizza**:
- **Simple Factory**: `factory/simple_factory` — encapsula `new` en una fábrica.
- **Factory Method**: `factory/factory_method` — `PizzaStore` abstracto + tiendas NY/Chicago.
- **Abstract Factory**: `factory/abstract_factory` — familias de ingredientes por región.

## Ejecutar
```bash
# Simple Factory
python -m factory.simple_factory.main

# Factory Method
python -m factory.factory_method.main

# Abstract Factory
python -m factory.abstract_factory.main
```

## TP (resumen)
1) Agregar variedades (veggie/pepperoni) en FM y AF.  
2) En AF, completar más ingredientes (veggies/pepperoni) y tests.  
3) Escribir 3–5 pruebas por flujo de orden (NY vs Chicago).

> Referencia: Clase 3 (PPT) y *Head First Design Patterns*, cap. 4.

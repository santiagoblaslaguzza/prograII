Explicación de los Observadores Concretos:

Cada display implementa las interfaces Observer y DisplayElement.

En __init__, se registra con el objeto WeatherData.

El método update es llamado por WeatherData cuando hay nuevos datos. Almacena los datos relevantes y luego llama a display.

El método display muestra la información específica de ese display.

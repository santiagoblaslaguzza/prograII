Explicación de WeatherData:

__init__: Inicializa una lista vacía para los observadores y los valores del clima.

register_observer: Añade un observador a la lista.

remove_observer: Elimina un observador de la lista.

notify_observers: Itera sobre los observadores y llama a su método update, pasando los nuevos datos del clima (modelo Push en esta implementación).

measurements_changed: Es invocado cuando los datos del clima cambian, y su única responsabilidad es llamar a notify_observers.

set_measurements: Simula la llegada de nuevos datos del clima y luego llama a measurements_changed.

Los métodos get_ serían útiles si optamos por un modelo Pull (ver más adelante).

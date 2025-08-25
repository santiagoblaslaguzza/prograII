# TO-DO: Ejercicio - Refactorizar al Modelo Pull del Patrón Observer

En este ejercicio, modificaremos la implementación actual del Patrón Observer, que utiliza un modelo "Push" (donde el Sujeto envía los datos a los Observadores), para convertirla en un modelo "Pull" (donde el Sujeto solo notifica el cambio, y los Observadores solicitan activamente los datos que necesitan).

## Objetivos del Ejercicio:

* Comprender las diferencias prácticas entre los modelos Push y Pull.
* Modificar las interfaces y clases existentes para implementar el modelo Pull.
* Observar cómo cambian las responsabilidades entre el Sujeto y los Observadores.

## Archivos Involucrados:

Trabajaremos principalmente con los siguientes archivos de nuestro repositorio:

1.  `clases_base_abstractas.py`: Contiene las definiciones de las clases base abstractas `Subject` y `Observer`.
2.  `Subject.py`: Contiene la clase `WeatherData` (nuestro Sujeto Concreto).
3.  `displays.py`: Contiene las clases `CurrentConditionsDisplay`, `StatisticsDisplay`, y `ForecastDisplay` (nuestros Observadores Concretos).
4.  `main.py`: Nuestro programa principal para probar la implementación.

## Pasos para la Refactorización:

Sigue estos pasos en orden. ¡Presta atención a cómo los cambios en un archivo pueden requerir ajustes en otros!

### ✏️ Paso 1: Modificar la Interfaz `Observer`

**Archivo a modificar:** `clases_base_abstractas.py`

Actualmente, el método `update` en la interfaz `Observer` espera recibir `temperature`, `humidity`, y `pressure` como argumentos. Para el modelo Pull, el observador ya no recibirá estos datos directamente.

1.  Cambia la firma del método `update` en la clase `Observer` para que no acepte ningún argumento (o, alternativamente, para que acepte una referencia al `Subject` si los observadores no almacenan ya una referencia a él). Por simplicidad en este ejercicio, no pasaremos argumentos.

    ```python
    # En clases_base_abstractas.py
    class Observer(ABC):
        @abstractmethod
        def update(self): # ¡Ya no recibe temperature, humidity, pressure!
            pass
    ```

### ✏️ Paso 2: Modificar la Notificación en `WeatherData` (Sujeto Concreto)

**Archivo a modificar:** `Subject.py`

El método `notify_observers` en `WeatherData` actualmente "empuja" los datos del clima a cada observador. Ahora, solo debe notificar que ha habido un cambio.

1.  Ajusta el método `notify_observers` en la clase `WeatherData` para que llame al método `update()` de cada observador sin pasarle argumentos.

    ```python
    # En Subject.py, dentro de la clase WeatherData
    def notify_observers(self):
        for observer in self._observers:
            observer.update() # ¡Llama a update sin argumentos!
    ```

### ✏️ Paso 3: Modificar los Observadores Concretos (`displays.py`)

**Archivos a modificar:** `displays.py`

Este es el cambio más significativo. Cada observador concreto ahora necesita:
1.  Asegurarse de tener una referencia al objeto `WeatherData` (ya lo hacen, a través de `self._weather_data`).
2.  Modificar su método `update` para que:
    * Ya no acepte `temperature`, `humidity`, y `pressure` como parámetros.
    * Utilice su referencia a `WeatherData` (`self._weather_data`) para llamar a los métodos `get_temperature()`, `get_humidity()`, y `get_pressure()` y así obtener los datos que necesita.

**3.1. `CurrentConditionsDisplay`**

```python
# En displays.py, dentro de la clase CurrentConditionsDisplay
def update(self): # Ya no recibe parámetros
    self._temperature = self._weather_data.get_temperature()
    self._humidity = self._weather_data.get_humidity()
    # self._pressure = self._weather_data.get_pressure() # Descomentar si este display lo necesita
    self.display()
```

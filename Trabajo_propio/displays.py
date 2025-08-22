from clases_base_abstractas import Observer, DisplayElement
from Subject import WeatherData

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = 0.0
        self._humidity = 0.0
        self._weather_data = weather_data # Mantiene una referencia al sujeto
        weather_data.register_observer(self)

    def update(self):
        self._temperature = self._weather_data.get_temperature()
        self._humidity = self._weather_data.get_humidity()
        self.display()

    def display(self):
        print(f"Current conditions: {self._temperature}°C degrees and {self._humidity}% humidity")

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._max_temp = -float('inf')
        self._min_temp = float('inf')
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self._temp_sum += self._weather_data.get_temperature()
        self._num_readings += 1
        self._max_temp = max(self._max_temp, self._weather_data.get_temperature())
        self._min_temp = min(self._min_temp, self._weather_data.get_temperature())
        self.display()

    def display(self):
        avg_temp = self._temp_sum / self._num_readings if self._num_readings > 0 else "N/A"
        print(f"Avg/Max/Min temperature = {avg_temp}/{self._max_temp}/{self._min_temp}")

class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._current_pressure = 29.92 # Presión por defecto
        self._last_pressure = 0.0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self._last_pressure = self._current_pressure
        self._current_pressure = self._weather_data.get_pressure()
        self.display()

    def display(self):
        forecast = ""
        if self._current_pressure > self._last_pressure:
            forecast = "Improving weather on the way!"
        elif self._current_pressure == self._last_pressure:
            forecast = "More of the same"
        elif self._current_pressure < self._last_pressure:
            forecast = "Watch out for cooler, rainy weather"
        print(f"Forecast: {forecast}")


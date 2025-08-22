def main():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    stats_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    print("Weather Station 1.0")
    print("-------------------")

    weather_data.set_measurements(26.6, 65, 30.4)
    print("---")
    weather_data.set_measurements(27.7, 70, 29.2)
    print("---")
    weather_data.set_measurements(25.5, 90, 29.2)

    # Ejemplo de desregistro (opcional)
    # print("\n--- Forecast display unsubscribed ---")
    # weather_data.remove_observer(forecast_display)
    # weather_data.set_measurements(28.0, 88, 30.0)

if __name__ == "__main__":
    main()

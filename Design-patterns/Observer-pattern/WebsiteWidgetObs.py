from Observer import Observer
from WeatherStation import WeatherStation

class WebsiteWidgetObs(Observer):
    def __init__(self, weatherStation: WeatherStation = None, observing: list[str] = []) -> None:
        self.weatherStation = weatherStation
        self.observing = observing
        if self.weatherStation is not None:
            self.weatherStation.add_observer(self)
        return

    def print_observingChange(self) -> None:
        print("Website widget: ")
        for obs in self.observing:
            if obs == 'Temperature':
                print(f"Temperature: {self.weatherStation.temperature}°C")
            elif obs == 'Humidity':
                print(f"Humidity: {self.weatherStation.humidity}%")
            elif obs == 'Pressure':
                print(f"Pressure: {self.weatherStation.pressure} hPa")
        return
    
    def set_weather_station(self, weatherStation: WeatherStation = None) -> bool:
        if weatherStation is not None:
            self.weatherStation = weatherStation
            if self.observing != []:
                self.weatherStation.add_observer(self)
            return True
        return False
    
    def remove_weather_station(self) -> bool:
        if self.weatherStation is not None:
            self.weatherStation.remove_observer(self)
            self.weatherStation = None
            return True
        return False
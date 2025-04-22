from Observer import Observer

class WeatherStation:
    def __init__(self, temperature: int = 0, humidity: int = 0, pressure: int = 0) -> None:
        self.observers = {
            'Temperature': [],
            'Humidity': [],
            'Pressure': []
        }
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        
    def add_observer(self, observer: Observer) -> None:
        observing = observer.observing
        if observing == []:
            return False
        
        for obs in observing:
            if obs in self.observers:
                self.observers[obs].append(observer)
        return True
        

    def remove_observer(self, observer: Observer) -> None:
        observing = observer.get_observing()
        if observing in self.observers:
            self.observers[observing].remove(observer)
            return True
        return False
    
    def notify_observers(self, change: str) -> None:
        if change in self.observers:
            for observer in self.observers[change]:
                observer.print_observingChange()
    
    def set_measurements(self, temperature: int = 0, humidity: int = 0, pressure: int = 0) -> None:
        if temperature != 0:
            self.temperature = temperature
            self.notify_observers('Temperature')
        if humidity != 0:
            self.humidity = humidity
            self.notify_observers('Humidity')
        if pressure != 0:
            self.pressure = pressure
            self.notify_observers('Pressure')
        return

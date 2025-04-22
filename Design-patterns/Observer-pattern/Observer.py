from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def print_observingChange():
        pass

    @abstractmethod
    def set_weather_station():
        pass

    @abstractmethod
    def remove_weather_station():
        pass

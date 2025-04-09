from abc import abstractmethod, ABC

class Notification(ABC):

    @abstractmethod
    def Notify(self):
        pass
from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    # def __init__ (self, last_service_date, EngineDelegate, BatteryDelegate)


    @abstractmethod
    def needs_service(self):
        pass
        # if self.engine.needs_service() || self.battery.needs_service :
        #     return true
        # else:
        #     return false





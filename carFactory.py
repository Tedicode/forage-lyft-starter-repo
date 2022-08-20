from abc import ABC, abstractmethod

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery



class Car(ABC):
    def __init__(self, EngineDelegate, BatteryDelegate):
        # self.last_service_date = last_service_date
        self.engine = EngineDelegate
        self.battery = BatteryDelegate

    @abstractmethod
    def needs_service(self):
        # pass
        if self.engine.needs_service() || self.battery.needs_service() :
            return true
        else:
            return false

class Calliope(Car) :
  def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage) :
    super().__init__(new CapuletEngine(current_mileage, last_service_mileage), new SpindlerBattery(last_service_date))
    self.current_date = current_date


class Glissade(Car) :
  def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage) :
    super().__init__(new WilloughbyEngine(current_mileage, last_service_mileage), new SpindlerBattery(last_service_date))
    self.current_date = current_date


class Palindrome(Car) :
  def __init__(self, current_date, last_service_date, warning_light_on) :
    super().__init__(new SternmanEngine(warning_light_on), new SpindlerBattery(last_service_date))
    self.current_date = current_date


class Rorschach(Car) :
  def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage) :
    super().__init__(new WilloughbyEngine(current_mileage, last_service_mileage), new NubbinBattery(last_service_date))
    self.current_date = current_date

class Thovex(Car) :
  def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage) :
    super().__init__(new CapuletEngine(current_mileage, last_service_mileage), new NubbinBattery(last_service_date))
    self.current_date = current_date

# ---------------------------------------------------------------
# class carFactory(Car) :
#   def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) :

#   def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)

#   def create_palindrome(current_date, last_service_date, warning_light_on)

#   def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)

#   def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)

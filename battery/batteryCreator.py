from abc import ABC, abstractmethod


class Battery(ABC) :
  def __init__(self, last_service_date, yearsBetweenService) :
    self.last_service_date = last_service_date
    self.yearsBetweenService = yearsBetweenService

  @abstractmethod
  def needs_service(self) :
    service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.yearsBetweenService)
    if service_threshold_date < datetime.today().date():
            return True
        else:
            return False







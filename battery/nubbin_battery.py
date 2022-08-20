from batteryCreator import Battery


yearsBetweenService = 4

class NubbinBattery(Battery) :
  def __init__(self, last_service_date) :
    super().__init__(last_service_date, yearsBetweenService)

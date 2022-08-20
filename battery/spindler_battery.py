from batteryCreator import Battery

yearsBetweenService = 2

class SpindlerBattery(Battery) :
  def __init__(self, last_service_date):
    super().__init__(last_service_date, yearsBetweenService)

from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_to_be_serviced_by = self.last_service_date + 4
        if date_to_be_serviced_by < self.current_date:
            return True
        else:
            return False
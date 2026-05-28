class ChargeController:

    def __init__(self):
        self.status = "idle"

    def start_charging(self):
        self.status = "charging"

    def stop_charging(self):
        self.status = "idle"

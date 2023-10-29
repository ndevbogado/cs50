class ship():
    def __init__(self, model, ship_class, hyper_drive, shields, weapons, hull):
        self.model = model
        self.ship_class = ship_class
        self.hyper_drive = hyper_drive
        self.shields = shields
        self.weapons = weapons
        self.hull = hull
    
    def specs(self):
        return f"{self.model} - {self.ship_class} - hyperdrive:{self.hyper_drive} - shields:{self.shields} - {self.weapons} - {self.hull}"


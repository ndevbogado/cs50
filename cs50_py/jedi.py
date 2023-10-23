class Force_User():
    def __init__(self, name, affinity):
        self.name = name
        self.affinity = affinity
        print(self.name, self.affinity)

class Jedi(Force_User):
    def __init__(self, name, affinity, lightsaber):
        super().__init__(name, affinity)
        self.lightsaber = lightsaber
        print(self.lightsaber)

class Jedi_Master(Jedi):
    def __init__(self, name, affinity, lightsaber, rank):
        super().__init__(name, affinity, lightsaber)
        self.rank = rank
        print(self.rank)

def main():
    citizen = Force_User("Ahsoka", "Force connection")
    no_master = Jedi("Anakin", "Chosen-One", "blue")
    grand_master = Jedi_Master("Yoda", "Force", "Green", "Grand Jedi Master")


if __name__ == "__main__":
    main()

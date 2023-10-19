import re

class Hero:
    def __init__(self, name, faction, force):
        self.name = name
        self.faction = faction
        self.force = force

    def __str__(self):
        return f"{self.name} from {self.faction}"
    
    def force_power(self):
        if re.match(r"^(L|l)ight(.+)?$", self.force):
            return "Force Pull"
        elif re.match(r"^(D|d)ark(.+)?$", self.force):
            return "Force Choke"
        else:
            return "No Force"

    @classmethod
    def get(cls):
        name = input("Name: ")
        faction = input("Faction: ")
        force = input("Force Alligment: ")

        return cls(name, faction, force)

def main():
    hero = Hero.get()
    print(hero.force_power())


if __name__ == "__main__":
    main()

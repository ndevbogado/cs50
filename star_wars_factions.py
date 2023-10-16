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
    
    @property
    def faction(self):
        return self._faction

    @faction.setter
    def faction(self, faction):
        if faction not in ["Empire", "Rebele Alliance", "Republic", "Separatist"]:
            raise ValueError("Invalid Faction")
        self._faction = faction

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name



def main():
    hero = get_hero()
    print(hero.force_power())

def get_hero():
    name = input("Name: ")
    faction = input("Faction: ")
    force = input("Force: ")
    
    hero = Hero(name, faction, force)    

    return hero

if __name__ == "__main__":
    main()

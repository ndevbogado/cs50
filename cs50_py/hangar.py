class Hangar:
    def __init__(self, fighters="Z95-Headhunter", bombers="BunkerBuster", gunships="LAAT", interceptors="Mandalorian Interceptor"):
        self.fighters = fighters
        self.bombers = bombers
        self.gunships = gunships
        self.interceptors = interceptors

    def __str__(self):
        return f"{self.fighters}, {self.bombers}, {self.gunships}, {self.interceptors}"
    
    def __add__(self, other):
        fighters = self.fighters + " " + other.fighters
        bombers = self.bombers + " " + other.bombers
        gunships = self.gunships + " " + other.gunships
        interceptors = self.interceptors + " " + other.interceptors

        return Hangar(fighters, bombers, gunships, interceptors)

def main():
    rebel_hangar = Hangar("X-Wings", "Y-Wings", "U-Wings", "A-Wings")
    print(rebel_hangar)

    imperial_hangar = Hangar("TIE fighter", "TIE bomber", "TIE reaper", "TIE interceptor")

    print(imperial_hangar)

    print(imperial_hangar + rebel_hangar)
if __name__ == "__main__":
    main()

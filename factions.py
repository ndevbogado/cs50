with open("factions.csv") as file:
    for line in file:
        hero,faction = line.rstrip().split(",")
        print(f"{hero} is a {faction}")     


heroes = []

with open("factions.csv") as file:
    for line in file:
        name,faction = line.rstrip().split(",")
        hero = {"name":name,"faction":faction}

        heroes.append(hero)

"""
def get_name(hero):
    return hero['name']
"""

for hero in sorted(heroes, key=lambda hero: hero["name"]):
    print(f"{hero['name']} is a {hero['faction']}")

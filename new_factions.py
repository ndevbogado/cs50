import csv

heroes = []

with open("factions.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        heroes.append({"name": row["hero"], "faction": row["faction"]})
for hero in sorted(heroes, key=lambda hero: hero["name"]):
    print(f"{hero['name']} is a {hero['faction']}")

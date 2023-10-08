import csv

heroes = []

with open("factions.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        heroes.append({"name": row[0], "faction": row[1]})
for hero in sorted(heroes, key=lambda hero: hero["name"]):
    print(f"{hero['name']} is a {hero['faction']}")

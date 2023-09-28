def main():
    
    heroes = [
        {"name": "Lord Vader", "afiliation": "Siths", "weapon": "Light Saber"},
        {"name": "Ahsoka", "afiliation": "Jedi", "weapon": "Force"},
        {"name": "Din Jarin", "afiliation": "Mandalorian", "weapon": "Gun Slinger"}
    ]

    for hero in heroes:
        
        print(hero["name"], hero["afiliation"], hero["weapon"], sep=", ")

main()

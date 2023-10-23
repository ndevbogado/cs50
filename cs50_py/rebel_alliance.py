def main():
    hero_list = format_hero_data(extract_hero_data())

    rebels = filter(is_rebel, hero_list)

    for rebel in rebels:
        print(rebel["name"])

def get_rebels():
    with open("./sw_heroes.csv", "r") as file:
        return [ row.split(",")[0] for row in file if "rebel alliance" in row]

def extract_hero_data():
    with open("./sw_heroes.csv", "r") as file:
        return [ row.replace("\n","") for row in file ]

def format_hero_data(hero_list_data):
    formated_list = []
    for hero in hero_list_data:
        hero_dict = {}
        name,faction=hero.split(",")
        hero_dict["name"] = f"{name}"
        hero_dict["faction"] = f"{faction}"

        formated_list.append(hero_dict)

    return formated_list

def is_rebel(hero_info):
    return hero_info["faction"] == "rebel alliance"


if __name__ == "__main__":
    main()

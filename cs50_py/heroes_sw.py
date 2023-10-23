import re

def main():
    for faction in read_factions():
        print(faction)

def read_factions():
    with open("./sw_heroes.csv", "r") as file:
        factions = set()
        for row in file:
            factions.add(re.split(r"^.+,", row)[1].replace("\n", ""))
        return factions

def input_data():
    with open("./sw_heroes.csv", "a") as file:
        while True:
            if (key_value := write_value("Name")) != None and (dict_value := write_value("Faction")) != None:
                file.write(f"{key_value},{dict_value}\n")
            if (continue_loop := input("Press Q to quit: ").lower()) == "q":
                break

def write_value(key_name):
    try:
        if (name:= input(f"{key_name}: ")) == "":
            raise ValueError
    except ValueError:
        print("Cannot write a blank name!")
        name = None
    finally:
        return name



if __name__ == "__main__":
    main()

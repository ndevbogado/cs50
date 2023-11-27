from abc import ABC, abstractclassmethod
import os

class Champion:
    def __init__(self, name, power):
        self.name = name.title()
        self.power = int(power)

    def power(self):
        return self.power

    def __add__(self, other):
        return Champion(self.name+other.name, ((self.power+other.power)/2)**2)

    def __str__(self):
        return f"Champion(name={self.name}, power={self.power})"

def champion_setter(counter):
    counter = counter + 1
    name = input(f"Type Champion's name {counter}: ")
    power = input(f"Type {name.title()}'s power: ")
    return Champion(name, power)


def main():

    while True:

        champions = [champion_setter(i) for i in range(2)]

        for champion in champions:
            print(champion)
        
        new_champion = champions[0] + champions[1]

        print("New Champion: ", new_champion)
        if input("Exit? (y/n)").upper() == "Y":
            os.system("clear")
            print("May the force be with you!")
            break


if __name__ == "__main__":
    main()

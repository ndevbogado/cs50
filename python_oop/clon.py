class Clon():
    def __init__(self, name, serial, rank, legion):
        self.name = name
        self.serial = serial
        self.rank = rank
        self.legion = legion

    def train(self):
        return f"{self.name.title()} is in traning session"

def main():

    attributes = input_attributes(4)
    cincos = Clon(*attributes)
    if input("Train? ") == "y":
        print(cincos.train())

def ask_for_attribute():
    return input("Set: ")

def input_attributes(length):
    return [ input("Set: ") for attribute in range(length)]


if __name__ == "__main__":
    main()

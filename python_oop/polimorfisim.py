class Cat():
    def sound(self):
        return "GG izi"

class Dog():
    def sound(self):
        return "Bonk"

def make_sound(animal):
    return animal.sound()

def main():
    yummi = Cat()
    nasus = Dog()

    print(make_sound(yummi))
    print(make_sound(nasus))

if __name__ == "__main__":
    main()

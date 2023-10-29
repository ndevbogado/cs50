class Animal:
    def __init__(self):
        print(self.eat())

    def eat(self):
        return "eating..."

class Mammal:
    def __init__(self):
        print(self.suckle())

    def suckle(self):
        return "suckling..."

class Bird:
    def __init__(self):
        print(self.fly())

    def fly(self):
        return "Flying..."

class Bat(Mammal, Bird, Animal):
    def __init__(self):
        Bird.__init__(self)
        Mammal.__init__(self)
        Animal.__init__(self)
    
    def batman(self):
        return "I'm the Night, I'm Vengance, I AM BATMAN"


def main():
    batman = Bat()
    print(batman.batman())

if __name__ == "__main__":
    main()

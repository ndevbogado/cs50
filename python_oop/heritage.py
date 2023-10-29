class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def speak(self):
        return f"Hello There! I'm {self.name}"

class IT_guy:
    def __init__(self, programming):
        self.programming = programming
    
    def tech_skill(self):
        return f"I know how to programm in {programming}"

class Physicist(Person, IT_guy):
    def __init__(self, name, age, nationality, programming):
        Person.__init__(self,name, age, nationality)
        IT_guy.__init__(self,programming)
    
    def greetings(self):
        return f"{super().speak()}"

def main():
    juanmadrosas = Physicist("juanma", 26, "argentinian", "python")
    print(juanmadrosas.greetings())

if __name__ == "__main__":
    main()

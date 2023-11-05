from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def __init__(self, name, age, gendre, job, activity):
        self.name = name
        self.age = age 
        self.gendre = gendre
        self.job = job
        self.activity = activity

    @abstractclassmethod
    def work(self):
        pass

    def presentation(self):
        return f"Hello There! My name is {self.name} y I'm {self.age} years old"

class Student(Person):
    def __init__(self, name, age, gendre, job, activity):
        super().__init__(name, age, gendre, job, activity)
    
    def work(self):
        return f"I'm currently: {self.activity}"

class Worker(Person):
    def __init__(self, name, age, gendre, job, activity):
        super().__init__(name, age, gendre, job, activity)

    def work(self):
        return f"I'm {self.job}"

def main():
    nightmare = Student("Nahu D. Bogado", 26, "M", "Salary adjuster", "studying python")
    juanma = Worker("JuanMa D. Rosas", 15, "M", "Physicist", "playing video games")

    print(nightmare.presentation(),nightmare.work())

    print(juanma.presentation(), juanma.work())


if __name__ == "__main__":
    main()

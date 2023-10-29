class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def print_info(self):
        return f"{self.get_name()}, {self.get_age()}"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def get_grade(self):
        return self.grade

    def print_grade(self):
        return f"{self.print_info()}, {self.grade}"


def main():

    MAX_VALUE = 3
    
    student = Student(*[input(f"Value {i+1}/{MAX_VALUE}: ") for i in range(MAX_VALUE)])
    print(student.print_grade())


if __name__ == "__main__":
    main()

import sys

class Person:
    def __init__ (self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    @name.deleter
    def name(self):
        print("property deleted!")
        del self.__name

def main():

    my_name = "XD"
    if len(sys.argv) == 2:
        my_name = sys.argv[1]
    nahu = Person(my_name, 26)

    print(f"My name is: {nahu.name}")

    del nahu.name
if __name__ == "__main__":
    main()

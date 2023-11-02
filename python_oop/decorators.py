def decorator(function):
    def modified_function():
        print("Before calling main function")
        function()
        print("After calling main function")

    return modified_function
"""
def salute():
    print("Hello There!")
"""

@decorator
def salute():
    print("Decorated Hello There!")
def main():
    salute()

if __name__ == "__main__":
    main()

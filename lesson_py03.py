def main():
    name = input("What's your name? ")
    hello()
    hello(name)


def hello(to="there!"):
    print(f"hello {to}")


main()

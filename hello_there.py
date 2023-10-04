def main():
    name = input("What's ypur name? ")
    hello(name)

def hello(to="General Kenobi!"):
    return f"Hello There! {to}"
    
if __name__ == "__main__":
    main()

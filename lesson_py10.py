def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt): 
    while True: 
        try:
            x = int(input(prompt))
        except ValueError:
            pass
            #print("x is not an integer")
        else:
            #this 'else' statement is realted to 'try' statement if its code goes right 
            return x
main()

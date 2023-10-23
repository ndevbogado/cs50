def main():
    print("xd1")
    my_value = get_value()
   
    while_count(my_value)

    for i in range(my_value):
        print(f"{i} for XD")
    
    print("XD\n" * my_value , end="")

def get_value():
    while True:
        my_value = int(input("Type number of repetition: "))
        if my_value > 0:
            return my_value
        print("Value must be greater than '0'! ")

def while_count(rep):
    count = 0
    while count < rep:
        print(f"{count} while XD")
        count += 1

main()

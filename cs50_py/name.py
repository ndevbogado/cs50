
while True:
    name = input("What's your name? ")
    if name == "q":
        break
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


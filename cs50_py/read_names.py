with open("names.txt", "r") as file:
    names = []
    for line in file:
        names.append(line.rstrip())
    
    for name in sorted(names):
        print(name)

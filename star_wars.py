import csv
import sys

def main():
    try:    
        file_name = sys.argv[1]
    except IndexError:
        print("Program needs a file input!\n\nExiting program now...")
        sys.exit()
    while True:
        menu = input("Choose an option:\n1- Print file's content\n2- Write file\n3- Exit Program\n\nChoose an option: ")
        if menu == "1":
            print_content(read_file(file_name))
        elif menu == "2":
            write_file(file_name)
        else:
            print("May The force be with You!")
            break

def write_file(file_name):
    name = input("What's your name?: ")
    home = input("Where's your home?: ")

    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, home])

        
def read_file(file_name):
    content = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            content.append({"name": row["name"], "home": row["home"]})
    return content

def print_content(file_content):
    for item in file_content:
        print(f"{item['name']} is from {item['home']}")
    print()
   
if __name__ == "__main__":
    main()

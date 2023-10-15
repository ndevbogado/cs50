import re

def main():
    name = formated_name(input("What's your name?: "))
    print(f"Hello There, {name}!")

def formated_name(name):
    name = name.strip()

    if matches := re.search(r"^(.+), *(.+)$", name):
        name = matches.group(2) + " " + matches.group(1)
    return name



if __name__ == "__main__":
    main()

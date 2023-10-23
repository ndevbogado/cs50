def main():
    name = input("What's your name? ")
    
    match name:
        case "Vader":
            print("Empire")
        case "Luke":
            print("Rebele Alliance")
        case "Din Jarin":
            print("Mandalorian")
        case _:
            print("No Alliances")
main()

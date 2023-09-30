import sys

def main():

    print("Hello There!\nGeneral", full_name())

def full_name():
    full_name = ""
    
    for name in sys.argv[1:]:
        full_name += f"{name} " 
    return full_name

main()

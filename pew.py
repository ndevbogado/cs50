import sys

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])

        for i in range(n):
            print("pew")
    else:
        print("usage: pew.py")


if __name__ == "__main__":
    main()

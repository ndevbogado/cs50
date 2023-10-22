import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Pew like a bolt weapon")
    parser.add_argument("-n", default=1, help="number of times to pew", type=int)
    args = parser.parse_args()

    for _ in range(args.n):
        print("pew")
if __name__ == "__main__":
    main()

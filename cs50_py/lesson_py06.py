def main():
    x = int(input("What's x? "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")
"""
#Normal version of the same is_even function:

def is_even(n):
    remainder = False
    if n % 2 == 0:
        remainder = True
    return remainder
"""

#shortest yet even valid version of is_even function:

def is_even(n):
    return n % 2 == 0


main()

from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("x was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("x was not 9")
    try:
        assert square(-1) == 1
    except AssertionError: 
        print("x was not 1")
    try:
        assert square(0) == 0
    except AssertionError:
        print("x was not 0")
        

if __name__ == "__main__":
    main()

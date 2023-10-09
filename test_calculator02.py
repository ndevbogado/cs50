from calculator import square

def main():
    test_positive()
    test_negative()
    test_zero()

def test_positive():   
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0)  == 0


main()
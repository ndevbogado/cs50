from hello_there import hello

def test_default():
    assert hello() == "Hello There! General Kenobi!"

def test_argument():
    assert hello("Nahu D. Bog") == "Hello There! Nahu D. Bog"

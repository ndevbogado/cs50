import sys
sys.path.append("../")

from format import formated_name


def test_format_name_01():
    assert formated_name("Bogado, Nahuel D.") == "Nahuel D. Bogado"

def test_formated_name_02():
    assert formated_name("Nahuel D. Bogado") == "Nahuel D. Bogado"

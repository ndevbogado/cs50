import sys

sys.path.append("../")

from validate import validate_email

def test_ok_01():
    assert validate_email("n_dev_bogado@gmail.com")

def test_ok_02():
    assert validate_email("ndevbogado@gmail.com.ar")

def test_ok_03():
    assert validate_email("ndevbogado97@gmail.com.ar")

def test_ok_04():
    assert validate_email("ndevbogado97@gmail.starwars.com.ar")

def test_wrong_01():
    assert validate_email("@gmail.com")

def test_wrong_02():
    assert validate_email("ndevbogado@")

def test_wrong_03():
    assert validate_email("ndevbogado@@@gmail.com")

def test_wrong_04():
    assert validate_email("ndev.bogado@gmail.com")

def test_wrong_05():
    assert validate_email("ndevbogado@gmailcom")

def test_wrong_06():
    assert validate_email("ndevbogado@gmail.xd")

def test_wrong_07():
    assert validate_email("ndevbogado@.com.ar")

def test_wrong_08():
    assert validate_email("ndevbogado@gmail..com.ar")





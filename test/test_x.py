import sys
sys.path.append("../")

from x import get_username


def test_url_ok_01():
    assert get_username("https://twitter.com/ndevbogado") == "ndevbogado"

def test_url_ok_02():
    assert get_username("http://www.twitter.com/ndevbogado") == "ndevbogado"

def test_url_ok_03():
    assert get_username("twitter.com/ndevbogado") == "ndevbogado"


from lib._04_debugging import *

# 1
def test_say_hello():
    result = say_hello("kay")
    assert result == "hello kay"

def test_encode():
    result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"


def test_decode():
    result1 = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert result1 == "theswiftfoxjumpedoverthelazydog"



def test_get_most_common_letter():
    result = get_most_common_letter("the roof, the roof, the roof is on fire!")
    print(f"Actual result: {result}")
    assert result == "o"
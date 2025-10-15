from plates import is_valid

def test_valid_extension():
    assert is_valid("AA23") == True
    assert is_valid("AEBT") == True
    assert is_valid("ASDFGBFRT") == False
    assert is_valid("A") == False


def test_valid_twoletters():
    assert is_valid("AA1212") == True
    assert is_valid("AE12") == True
    assert is_valid("1221EE") == False
    assert is_valid("E1212") == False


def test_is_alphanumeric():
    assert is_valid("AAJH") == True
    assert is_valid("AE28") == True
    assert is_valid("CR-4") == False
    assert is_valid("EBE?") == False


def test_numposition():
    assert is_valid("AA1212") == True
    assert is_valid("AE1212") == True
    assert is_valid("PRDE2P") == False
    assert is_valid("AD02EF") == False


def test_zeros():
    assert is_valid("AA10") == True
    assert is_valid("AE21") == True
    assert is_valid("PR02") == False
    assert is_valid("AD02EF") == False

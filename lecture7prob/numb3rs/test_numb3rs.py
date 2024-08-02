from numb3rs import validate

def test_range():
    assert validate("0.1.2.3") == True
    assert validate("255.254.255.254") == True
    assert validate("0.0.0.0") == True
    assert validate("256.1.2.3") == False
    assert validate("1.256.3.4") == False
    assert validate("1.2.256.4") == False
    assert validate("1.2.3.256") == False

def test_format():
    assert validate("....") == False
    assert validate("0?1!2@3") == False
    assert validate("cat") == False
    assert validate("25A.56.21@.155") == False
    assert validate("  1.  2  . 3  . 4") == False

def test_length():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2") == False

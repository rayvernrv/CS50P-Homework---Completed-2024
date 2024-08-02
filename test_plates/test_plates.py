from plates import is_valid

def test_first_two_alpha():
    assert is_valid("malibu") == True
    assert is_valid("ma1234") == True
    assert is_valid("12mali") == False
    assert is_valid("123456") == False

def test_length():
    assert is_valid("mali") == True
    assert is_valid("ma") == True
    assert is_valid("malibum") == False
    assert is_valid("m") == False

def test_number_location():
    assert is_valid("ma1234") == True
    assert is_valid("ma12li") == False

def test_zero_location():
    assert is_valid("ma1012") == True
    assert is_valid("ma0123") == False

def test_punctuations():
    assert is_valid("ma,l?i") == False

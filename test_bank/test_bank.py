from bank import value


def test_hello():
    assert value("hello there") == 0


def test_startswith_h():
    assert value("hey there") == 20


def test_random():
    assert value("Who are you?") == 100
    assert value("1234") == 100


def test_case_sensitivity():
    assert value("Hello there") == 0
    assert value("HELLO") == 0
    assert value("Hey there") == 20

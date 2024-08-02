from um import count


def test_case():
    assert count("um um") == 2
    assert count("UM UM UM") == 3


def test_punc():
    assert count("um..um? um") == 3
    assert count("!um?") == 1


def test_words():
    assert count("Um, I am your mum, um, with no humor") == 2
    assert count("I am your mum, with no humor") == 0

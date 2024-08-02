from test.helloV3 import hello
from test.helloV3 import title_case

def test_argument():
    assert hello("David") == "hello, David"

def test_argument2():
    for name in ["Bubu","Yier","Avoca", "Labong"]:
        assert hello(name) == f"hello, {name}"

def test_default():
    assert hello() == "hello, world"

def test_title():
    assert title_case("david") == "David"

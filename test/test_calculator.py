import pytest
from test.calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(1.5) == 2.25

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): #when the code forgets to set user input to int
        square("cat")
#but this only test the square function. ValueError wont work here because it's an error in main()
#as TypeError is raised because return n * n expects numbers

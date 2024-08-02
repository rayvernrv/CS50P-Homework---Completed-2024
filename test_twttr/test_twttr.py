from twttr import shorten

def test_shorten():
    assert shorten("education") == "dctn"


def test_shorten_upperlower():
    assert shorten("EDUCATION") == "DCTN"
    assert shorten("EdUcAtIOn") == "dctn"
    assert shorten("eDuCaTioN") == "DCTN"

def test_shorten_novowels():
    assert shorten("dctn") == "dctn"


def test_shorten_with_number():
    assert shorten("education50") == "dctn50"


def test_shorten_with_punc():
    assert shorten("Hello!?.:") == "Hll!?.:"

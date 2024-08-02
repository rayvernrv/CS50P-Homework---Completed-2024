from seasons import convert_text


def test_output():
    assert convert_text(1234) == "One thousand, two hundred thirty-four minutes"

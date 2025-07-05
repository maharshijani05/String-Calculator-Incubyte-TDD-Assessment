from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("10") == 10

def test_two_numbers():
    assert add("1,2") == 3


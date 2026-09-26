from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0

def test_h():
    assert value("h") == 20

def test_other():
    assert value("") == 100

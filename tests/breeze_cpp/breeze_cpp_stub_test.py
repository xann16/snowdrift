from snowdrift.breeze_cpp.stub import hello, answer


def test_hello():
    assert hello(5) == "Hello from breeze (C++)! The answer is 5!"


def test_answer():
    assert answer() == 42

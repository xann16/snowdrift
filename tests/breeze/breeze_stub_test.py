from snowdrift.breeze.stub import hello, answer


def test_hello():
    assert hello(5) == "Hello from breeze! The answer is 5!"


def test_answer():
    assert answer() == 42

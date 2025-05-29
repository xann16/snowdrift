from snowdrift.core.stub import hello, answer


def test_hello():
    assert hello(5) == "Hello from snowdrift core! The answer is 5!"


def test_answer():
    assert answer() == 42

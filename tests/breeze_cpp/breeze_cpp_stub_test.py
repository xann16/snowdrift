from snowdrift.breeze_cpp.stub import answer, hello


def test_hello() -> None:
    assert hello(5) == 'Hello from breeze (C++)! The answer is 5!'


def test_answer() -> None:
    assert answer() == 42

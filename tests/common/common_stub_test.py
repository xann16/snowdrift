from snowdrift.common.stub import answer, hello


def test_hello() -> None:
    assert hello(5) == 'Hello from common! The answer is 5!'


def test_answer() -> None:
    assert answer() == 42

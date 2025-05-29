from snowdrift.code_writer.stub import hello, answer


def test_hello():
    assert hello(5) == "Hello from code writer! The answer is 5!"


def test_answer():
    assert answer() == 42

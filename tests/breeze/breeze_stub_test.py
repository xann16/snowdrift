"""Tests for snowdrift.breeze.stub."""

from snowdrift.breeze.stub import AnswerBox, hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello(5) == 'Hello from breeze! The answer is 5!'


def test_answer() -> None:
    """Test the answer function."""
    assert AnswerBox().answer() == 42


def test_answer_par() -> None:
    """Test the answer function."""
    assert AnswerBox(answer=100).answer() == 100

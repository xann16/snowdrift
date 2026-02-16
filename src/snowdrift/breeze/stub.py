"""Docstring for snowdrift.breeze."""


def hello(x: int) -> str:
    """Sample hello function to test that the module is working correctly.

    .. code-block:: python

        x = 2
        assert x == 2

    Failing example:

    >>> print(5 + 7)
    12

    .. doctest::

        >>> print(1 + 7)
        8


    """
    return f'Hello from breeze! The answer is {x}!'


class AnswerBox:
    """Sample AnswerBox class to test that the module is working correctly."""

    def __init__(self, answer: int = 42) -> None:
        """Initialize the AnswerBox with a default answer of 42.

        Args:
            answer (int): The answer to be stored in the box. Default is 42.

        """
        self._answer = answer

    def answer(self) -> int:
        """Return the answer stored in the AnswerBox.

        Returns:
            int: The answer stored in the AnswerBox.

        """
        return self._answer

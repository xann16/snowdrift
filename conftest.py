from doctest import ELLIPSIS

from sybil import Sybil
from sybil.parsers.rest import DocTestParser, PythonCodeBlockParser
from sybil.parsers.markdown import PythonCodeBlockParser as MarkdownCodeBlockParser

pytest_collect_file = Sybil(
    parsers=[DocTestParser(optionflags=ELLIPSIS), PythonCodeBlockParser(), MarkdownCodeBlockParser()],
    patterns=['*.rst', '*.md', '*.py'],
).pytest()

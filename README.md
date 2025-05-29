# snowdrift
Python package for generating optimized settings handlers (especially for HPC use) in C++ and other languages.

# Quick Dev Basics (WIP)

Initial dev setup:

```shell
uv sync --frozen
uv run pre-commit install --install-hooks
```

Running tests:

```shell
uv run pytest
```

or with code coverage report (exported to HTML):

```shell
uv run pytest --cov=src/snowdrift --cov-report html
```

Manually running `pre-commit` checks (including `ruff` linting / formatting and `mymp` type checking):

```shell
uv run pre-commit run -a
```

Running snowdrift CLI:

```shell
uv run snowdrift
```

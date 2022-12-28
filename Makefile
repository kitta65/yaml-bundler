.PHONY: test
test:
	poetry run black . --check && \
	poetry run flake8 && \
	poetry run mypy ./**/*.py --strict && \
	poetry run pytest

.PHONY: fmt
fmt:
	poetry run black .

.PHONY: setup
setup:
	# https://python-poetry.org/docs/#installation
	command -v poetry || curl -sSL https://install.python-poetry.org | python3 -
	poetry install

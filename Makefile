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
	./scripts/setup.sh

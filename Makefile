.PHONY: test
test:
	poetry run pytest && \
	poetry run mypy ./**/*.py --strict && \
	poetry run black . --check && \
	poetry run flake8

.PHONY: fmt
test:
	poetry run black .

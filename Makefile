.PHONY: help format install lint test

help:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

format:
	poetry run isort --profile black .
	poetry run black .

install:
	poetry install

lint:
	poetry run isort --profile black -c --diff .
	poetry run black --check .
	poetry run flake8 .

test:
	poetry run pytest --cov=datasette_mailto_links --cov-report term --cov-report xml ./tests

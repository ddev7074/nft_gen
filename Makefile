PYTHONPATH = PYTHONPATH=./
POETRY_RUN = poetry run

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

.PHONY: install
install:
	poetry install

.PHONY: images
images:
	poetry run python main.py

.PHONY: metadata
metadata:
	poetry run python metadata.py

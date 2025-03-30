default:
	poetry run python scrape.py

install:
	poetry install

update:
	poetry install --no-root

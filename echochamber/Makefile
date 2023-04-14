.PHONY: run

run:
	SLEEP_TIME=2 PERSONALITY=interesting poetry run python echochamber/main.py

run-emo:
	PERSONALITY=emotional poetry run python echochamber/main.py

run-interesting:
	PERSONALITY=interesting poetry run python echochamber/main.py

lint:
	poetry run pylint echochamber tests

format:
	poetry run black echochamber tests && poetry run isort echochamber tests
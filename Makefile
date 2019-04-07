all: check_codestyle run_tests
	python3 ./app.py

run_tests: check_codestyle
	python3 ./run_tests.py

check_codestyle:
	flake8 *.py modules/*.py tests/*.py

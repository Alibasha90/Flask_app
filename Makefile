# target: dependencies
#   command

SHELL := /bin/bash
#step 1: create virtual environment
venv:
	python3 -m venv venv 
#step 2: activate virtual environment
switch:
	source venv/bin/activate
#step 3: install dependencies
install:
	./venv/bin/pip install -r requirements.txt
#step 4: run the application
run: 
	python3 main.py

freeze:
	pip freeze > requirements.txt
#step 5: clean up
clean:
	rm -rf __pycache__ *.pyc venv

all:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/python3 main.py
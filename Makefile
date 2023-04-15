install:
	pip install -r requirements.txt

format:	
	black app/**/*.py

lint:
	pylint --disable=R, app/*.py

refactor: 
	format lint

build:
	uvicorn app.main:app --reload

all: install lint format build
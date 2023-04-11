install:
	pip install -r requirements.txt

format:	
	black data/*.py api.py

lint:
	pylint --disable=R, api.py data/*py

refactor: format lint
		
all: install lint format
install:
	pip install -r requirements.txt

format:	
	black app/api.py app/data/*py

lint:
	pylint --disable=R, app/api.py app/data/*py

refactor: format lint
		
all: install lint format
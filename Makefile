install:
	pip install -r requirements.txt

format:	
	black app/*py

lint:
	pylint --disable=R, app/*py

refactor: format lint
		
all: install lint format
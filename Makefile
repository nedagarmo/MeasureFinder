install:
	pip install -r requirements.txt

run:
	set -a; source .env; set +a && cd src && python main.py

test:
	set -a; source .env; set +a && pytest -s
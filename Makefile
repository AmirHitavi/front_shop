flake8:
	flake8 --ignore=F405 .

black:
	black .

isort:
	isort .

base:
	pip install -r ./requirements/base.txt

local:
	pip install -r ./requirements/local.txt

production:
	pip install -r ./requirements/production.txt

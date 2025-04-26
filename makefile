PIP_VENV=.venv/bin/pip
PYTHON_VENV=.venv/bin/python

setup:
	python -m venv .venv
	
	$(PIP_VENV) install -r requirements.txt

run: 
	python main.py

test:
	python -m unittest tests/metodo.py

update_dep:
	pip freeze > requirements.txt

nix_env:
	nix run github:nix-community/pip2nix -- generate -r requirements.txt

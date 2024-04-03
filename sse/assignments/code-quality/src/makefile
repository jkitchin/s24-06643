black: 
	black .

flake8:
	flake8 --extend-ignore F401 --exclude build,.ipynb_checkpoints  .
    
pylint:
	pylint --ignore build s23bib
    
test:
	pytest .

all: black flake8 pylint test

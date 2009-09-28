all: install test

install:
	@python setup.py install

test:
	@python src/specs/run_specs.py
	@cd src/specs/console_examples && python run_examples.py

all: install test

install:
	@python setup.py install

test:
	@python specs/run_specs.py
	@cd specs/console_examples && python run_examples.py

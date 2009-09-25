all: install test

install:
	@python setup.py install

test:
	@python src/specs/run_tests.py
	@cd src/specs/console_examples && python run_examples.py

all: spec console

install:
	@python setup.py install

spec: install
	@python specs/run_specs.py

console: install
	@cd specs/console_examples && python run_examples.py

.PHONY: clean help lint

help:
	@echo "  clean      remove unwanted stuff"
	@echo "  lint       check the source for style errors"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name 'dist' -exec rm -r {} +
	find . -name '*.egg-info' -exec rm -r {} +

lint:check
	flake8

check:
	@type flake8 >/dev/null 2>&1 || echo "Flake8 is not installed. You can install it with 'pip install flake8'."

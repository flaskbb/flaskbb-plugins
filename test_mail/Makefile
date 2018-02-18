.PHONY: clean help test lint docs update-translations compile-translations add-translation wheel upload

help:
	@echo "  clean                  remove unwanted stuff"
	@echo "  test                   run the testsuite"
	@echo "  lint                   check the source for style errors"
	@echo "  docs                   build the documentation"
	@echo "  update-translations    updates the translations"
	@echo "  compile-translations   compiles the translations"
	@echo "  add-translation        adds a new language to the translations"
	@echo "  wheel                  creates a python wheel"
	@echo "  upload                 uploads the a python wheel to PyPI"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

test:
	py.test

docs:
	$(MAKE) -C docs html

lint:check
	flake8

check:
	@type flake8 >/dev/null 2>&1 || echo "Flake8 is not installed. You can install it with 'pip install flake8'."

update-translations:
	pybabel extract -F babel.cfg -k lazy_gettext -o test_mail/translations/messages.pot .
	pybabel update -i test_mail/translations/messages.pot -d test_mail/translations/

add-translation:
	@read -p "Enter new language shortcode:" lang; \
	pybabel init -i test_mail/translations/messages.pot -d test_mail/translations/ -l $$lang

compile-translations:
	pybabel compile -d test_mail/translations/

wheel:
	python setup.py bdist_wheel

upload:wheel
	twine upload dist/*

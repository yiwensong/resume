.PHONY: venv
venv:
	tox -e venv

.PHONY: install-hooks
install-hooks:
	tox -e install-hooks

.PHONY: test
test:
	tox

.PHONY: clean
clean:
	rm -rf .tox
	rm -rf venv
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	find . -name '*.pyc' | xargs rm -rf
	find . -name '__pycache__' | xargs rm -rf

.PHONY: build
build: venv
	venv/bin/generate-resume-pdf

.PHONY: dist
dist: venv
	venv/bin/python setup.py sdist bdist_wheel

upload_to_pypi: venv dist
	venv/bin/twine upload dist/*

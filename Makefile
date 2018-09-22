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
	find . -name '*.pyc' | xargs rm -rf
	find . -name '__pycache__' | xargs rm -rf

.PHONY: build
build: venv
	venv/bin/generate-resume-pdf

.PHONY: test unittests flaketest doctest ansibletest

test: unittests flaketest doctest ansibletest

unittests:
	coverage run ./publicdb/manage.py test tests.test_api

flaketest:
	flake8

doctest:
	PYTHONPATH=$(CURDIR):$(PYTHONPATH) sphinx-build -anW doc doc/_build/html

ansibletest:
	ansible-lint -p provisioning/playbook.yml || true

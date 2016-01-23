# Copyright (C) 2016 srforge project developers.
#
# See the COPYRIGHT file at the top-level directory of this distribution and at
# https://github.com/alunduil/srforge/blob/master/COPYRIGHT
#
# srforge is freely distributable under the terms of an MIT-style license.
# See LICENSE or http://www.opensource.org/licenses/mit-license.php.

nosetests_arguments = $(NOSETESTS_ARGUMENTS)

.PHONY: check
check: lint commit integration acceptance

.PHONY: lint
lint:
	pylint srforge srforge_tests setup.py

.PHONY: commit
commit: lint unit

.PHONY: unit
unit:
	nosetests -x srforge_tests/unit_tests $(nosetests_arguments)

.PHONY: integration
integration:
	nosetests -x srforge_tests/integration_tests $(nosetests_arguments)

.PHONY: acceptance
acceptance:
	behave srforge_tests/features

.PHONY: doc
docs: docs/build

docs/build:
	SPHINXOPTS='-n -W' make -eC docs html

.PHONY: clean
clean:
	find . -name '*.py[co]' -delete
	find . -name __pycache__ -delete
	rm -rf build dist srforge.egg-info
	make -eC docs clean

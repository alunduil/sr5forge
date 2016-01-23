Description
===========

Shadowrun Character Forge

A library with a factory for Shadowrun characters that can be serialized and
updated over time.

Installation
============

This package can be installed from PyPi::

    pip install srforge

If you would prefer to clone this package directly from git or assist with
development, the URL is https://github.com/alunduil/srforge.

Usage
=====

This package is a library and not intended for use on its own.  Evenutally, it
may contain clients for performing basic actions.

Checks
======

Checking the code is handled by a Makefile and has a few interesting targets:

:``check``:       all test suites
:``lint``:        linter
:``commit``:      all tests that are quick and should be run for every commit
                  (this is what should be called from a pre-commit hook)
:``unit``:        unit tests
:``integration``: integration tests

Known Issues
============

Known issues can be found in the github issue list at
https://github.com/alunduil/srforge.

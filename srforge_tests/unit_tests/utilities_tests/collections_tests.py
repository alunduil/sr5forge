# pylint: disable=missing-docstring
#
# Copyright (C) 2016 srforge project developers.
#
# See the COPYRIGHT file at the top-level directory of this distribution and at
# https://github.com/alunduil/srforge/blob/master/COPYRIGHT
#
# srforge is freely distributable under the terms of an MIT-style license.
# See LICENSE or http://www.opensource.org/licenses/mit-license.php.

import hypothesis
import hypothesis.strategies
import unittest

from srforge.utilities import collections


class TestEnsureUpper(unittest.TestCase):
    @hypothesis.given(hypothesis.strategies.text())
    def test_text(self, text):
        '''srforge.utilities.collections.ensure_upper(TExT) == TEXT.upper()'''

        self.assertEqual(text.upper(), collections.ensure_upper(text))

    @hypothesis.given(hypothesis.strategies.one_of(
        hypothesis.strategies.integers(),
        hypothesis.strategies.none(),
        hypothesis.strategies.booleans(),
        hypothesis.strategies.floats(allow_nan = False)
    ))
    def test_not_text(self, not_text):
        '''srforge.utilities.collections.ensure_upper(NOT_TEXT) == NOT_TEXT'''

        self.assertEqual(not_text, collections.ensure_upper(not_text))


class TestCaselessMappingConstructor(unittest.TestCase):
    @hypothesis.given(hypothesis.strategies.dictionaries(hypothesis.strategies.text(), hypothesis.strategies.text()))
    def test_caseless_from_dict(self, dictionary):
        '''srforge.utilities.collections.CaselessMapping(DICTIONARY)'''

        cm = collections.CaselessMapping(dictionary)  # pylint: disable=invalid-name

        for k in dictionary:  # pylint: disable=invalid-name
            self.assertEqual(cm[k.upper()], dictionary[k])
            self.assertEqual(cm[k.lower()], dictionary[k])
            self.assertEqual(cm[k], dictionary[k])


class TestCaselessMappingMethods(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.cm = collections.CaselessMapping()  # pylint: disable=invalid-name

    @hypothesis.given(
        hypothesis.strategies.text(),
        hypothesis.strategies.text()
    )
    def test_set_and_get_item(self, key, value):
        '''srforge.utilities.collection.CaselessMapping().__getitem__(KEY) == VALUE'''

        self.cm[key] = value

        self.assertEqual(self.cm[key], value)

        self.assertEqual(self.cm[key.upper()], value)
        self.assertEqual(self.cm[key.lower()], value)

    def test_delitem(self):
        '''srforge.utiltiies.collection.CaselessMapping().__delitem__(KEY)'''

        self.cm['test'] = 'something'

        self.assertEqual('something', self.cm['test'])

        del self.cm['test']

        self.assertNotIn('test', self.cm)

    def test_pop(self):
        '''srforge.utilities.collections.CaselessMapping().pop(KEY) == VALUE'''

        self.cm['test'] = 'something'

        self.assertEqual('something', self.cm.pop('test'))
        self.assertNotIn('test', self.cm)

    def test_get(self):
        '''srforge.utilties.collections.CaselessMapping().get(KEY) == VALUE'''

        self.cm['test'] = 'something'

        self.assertEqual('something', self.cm.get('test'))
        self.assertIn('test', self.cm)

    def test_setdefault(self):
        '''srforge.utilities.collections.CaselessMapping().setdefault(KEY, VALUE) == VALUE'''

        self.cm.setdefault('test', 'something')

        self.assertEqual('something', self.cm.setdefault('test', 'something else'))
        self.assertEqual('something', self.cm.setdefault('test', 'something else'))

    def test_update(self):
        '''srforge.utilities.collections.CaselessMapping().update(MAPPING)'''

        self.cm.update({ 'a': 'a', })
        self.cm.update(b = 'b')

        self.assertEqual('a', self.cm['a'])
        self.assertEqual('b', self.cm['b'])

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


class TestCaselessMapping(unittest.TestCase):
    @hypothesis.given(hypothesis.strategies.dictionaries(hypothesis.strategies.text(), hypothesis.strategies.text()))
    def test_caseless(self, dictionary):
        '''srforge.utilities.collections.CaselessMapping(DICTIONARY)'''

        cm = collections.CaselessMapping(dictionary)  # pylint: disable=invalid-name

        for k in dictionary:  # pylint: disable=invalid-name
            self.assertEqual(cm[k.upper()], dictionary[k])
            self.assertEqual(cm[k.lower()], dictionary[k])
            self.assertEqual(cm[k], dictionary[k])

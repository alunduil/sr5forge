# Copyright (C) 2016 srforge project developers.
#
# See the COPYRIGHT file at the top-level directory of this distribution and at
# https://github.com/alunduil/srforge/blob/master/COPYRIGHT
#
# srforge is freely distributable under the terms of an MIT-style license.
# See LICENSE or http://www.opensource.org/licenses/mit-license.php.

'''Helpful Collections.

**Functions**

:`ensure_upper`: ensure passed thing is uppercase if possible

**Classes**

:`CaselessMapping`: case-insenstive mapping

'''

import typing  # use mypy typing—pylint: disable=unused-import

from typing import Any


def ensure_upper(thing: Any) -> Any:
    '''Ensure thing passed is uppercase if it is case aware.

    **Arguments**

    :``thing``: any python value

    **Return Value(s)**

    Uppercase version of thing if thing is case aware; otherwise, thing.

    '''

    result = thing

    try:
        result = thing.upper()
    except AttributeError:
        pass

    return result


class CaselessMapping(dict):
    '''Case-insensitive map.

    This acts exactly like a standard dictionary but any case aware keys will be
    upper cased for entry and retrieval.  This means that given a key, 'A', both
    'A' and 'a' can be used to lookup the same value.

    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key in list(self.keys()):
            self.__setitem__(key, super().pop(key))

    def __getitem__(self, key):
        return super().__getitem__(ensure_upper(key))

    def __setitem__(self, key, item):
        super().__setitem__(ensure_upper(key), item)

    def __delitem__(self, key):
        super().__delitem__(ensure_upper(key))

    def __contains__(self, key):
        return super().__contains__(ensure_upper(key))

    def pop(self, key, *args, **kwargs):
        return super().pop(ensure_upper(key), *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return super().get(ensure_upper(key), *args, **kwargs)

    def setdefault(self, key, *args, **kwargs):
        return super().setdefault(ensure_upper(key), *args, **kwargs)

    def update(self, E = None, **F):
        if E is not None:
            super().update(self.__class__(E))

        super().update(self.__class__(**F))

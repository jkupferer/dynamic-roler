from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible import errors

def test_galaxy_source(role):
    return True

def test_volatile_version(role):
    return True

class TestModule(object):
    def tests(self):
        return dict(
            galaxy_source=test_galaxy_source,
            volatile_version=test_volatile_version
        )


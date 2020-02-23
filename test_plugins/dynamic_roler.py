from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible import errors

import re

def dynamic_roler_galaxy_source(role):
    return 'git' not in role

def dynamic_roler_cache_disabled(role):
    '''
    Return whether cache is enabled for this role.
    Cache may be enabled explicitly or otherwise detected from the version string.
    Versions that appear to use semantic versioning will be enabled for cache.
    '''
    if 'cache' in role:
        return not role['cache']
    elif 'version' not in role:
        return True
    elif re.search(r'\d+\.\d+\.\d+', role['version']):
        return False
    else:
        return True

class TestModule(object):
    def tests(self):
        return dict(
            dynamic_roler_galaxy_source=dynamic_roler_galaxy_source,
            dynamic_roler_cache_disabled=dynamic_roler_cache_disabled
        )

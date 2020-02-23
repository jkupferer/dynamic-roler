from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible import errors

import re

def dynamic_roler_galaxy_source(role):
    return 'git' not in role

def dynamic_roler_git_source(role):
    return 'git' in role

def dynamic_roler_cache_enabled(source):
    '''
    Return whether cache is enabled for this source.
    Cache may be enabled explicitly or otherwise detected from the version string.
    Versions that appear to use semantic versioning will be enabled for cache.
    '''
    if 'cache' in source:
        return bool(source['cache'])
    elif 'git' in source:
        source = source['git']
    if 'version' not in source:
        return False
    elif re.search(r'\d+\.\d+\.\d+', source['version']):
        return True
    else:
        return False

def dynamic_roler_cache_disabled(source):
    '''
    Return whether cache is disbled for this source.
    '''
    return not dynamic_roler_cache_enabled(source)

class TestModule(object):
    def tests(self):
        return dict(
            dynamic_roler_cache_disabled=dynamic_roler_cache_disabled,
            dynamic_roler_cache_enabled=dynamic_roler_cache_enabled,
            dynamic_roler_galaxy_source=dynamic_roler_galaxy_source,
            dynamic_roler_git_source=dynamic_roler_git_source
        )

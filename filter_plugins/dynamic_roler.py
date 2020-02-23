# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

import hashlib
import re
from ansible.errors import AnsibleFilterError

def dynamic_roler_source_name(source):
    if 'name' in source:
        return source['name']
    m = re.search(r'/(\w+)(\.git)?$', source['src'])
    if m:
        return m.group(1)
    elif re.match('(\w+)\.(\w+)$', source['src']):
        return source['src']
    raise AnsibleFilterError("Unable to determine source name from {}, name must be provided".format(source['src']))

def dynamic_roler_git_source_repo_hash(source):
    git = source['git']
    name = dynamic_roler_source_name(source)
    m = re.search(r'/(\w+)(\.git)?$', git['repo'])
    prefix = m.group(1) + '-'
    if 'version' in git:
        prefix += git['version'] + '-'
    return prefix + hashlib.sha256((
        git['repo'] + ':' + git.get('version', '')
    ).encode('utf-8')).hexdigest()

# ---- Ansible filters ----
class FilterModule(object):

    def filters(self):
        return {
            'dynamic_roler_git_source_repo_hash': dynamic_roler_git_source_repo_hash,
            'dynamic_roler_source_name': dynamic_roler_source_name
        }

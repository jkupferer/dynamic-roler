# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

import re
from ansible.errors import AnsibleFilterError

def dynamic_role_name(role):
    if 'name' in role:
        return role['name']
    m = re.search(r'/(\w+)(\.git)?$', role['src'])
    if m:
        return m.group(1)
    raise AnsibleFilterError("Unable to determine role name from {}, name must be provided".format(role['src']))

# ---- Ansible filters ----
class FilterModule(object):

    def filters(self):
        return {
            'dynamic_role_name': dynamic_role_name
        }

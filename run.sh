#!/bin/sh

DIR="dynamic_roler_$$"

export ANSIBLE_ROLES_PATH="$(realpath ${DIR}):${ANSIBLE_ROLES_PATH:-~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles}"

ansible-playbook $(dirname $0)/playbook.yaml -e dynamic_roler_tmpdir="${DIR}" "$@"

rm -rf ${DIR}

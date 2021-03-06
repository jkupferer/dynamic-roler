#!/bin/sh

DIR="dynamic_roler_$$"

echo $DIR

export ANSIBLE_ROLES_PATH="$(realpath ${DIR}):${ANSIBLE_ROLES_PATH:-~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles}"

ansible-playbook $(dirname $0)/manual-setup.yaml -e dynamic_roler_tmpdir="${DIR}"

# -*- coding: utf-8 -*-
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase


class CannotBePickled:
    def __getstate__(self):
        raise Exception('pickle intentionally not supported')


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        return {'obj': CannotBePickled()}

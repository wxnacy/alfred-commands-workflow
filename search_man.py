#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sys
import json
import os
import logging

from workflow import Workflow3

def read_json(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return json.loads(''.join(lines))

def main(wf):
    args = wf.args
    cmd = args[0]

    man = read_json('./man.json')

    default = man.pop('default')

    if cmd == 'git':
        for item in man['git']:
            url = item['subtitle']
            git_cmd = '-'.join(args[0:2])
            url = url.format(git_cmd)
            if len(args) == 3 and 'git-scm' in url:
                url = '{}#Documentation/{}.txt-{}'.format(
                        url, git_cmd, args[-1])
            item['subtitle'] = url
            item['arg'] = url
            item['valid'] = True
            wf.add_item(**item)

    if cmd == 'vagrant':
        for item in man['vagrant']:
            if len(args) == 1:
                url = 'https://www.vagrantup.com/docs/cli/'
            if len(args) >= 2:
                url = item['subtitle']
                git_cmd = args[1]
                url = url.format(git_cmd)
            item['subtitle'] = url
            item['arg'] = url
            item['valid'] = True
            wf.add_item(**item)

    for item in default:
        url = item['subtitle']
        ss = '-'
        cmd_excludes = item.pop('cmd_excludes', [])
        if cmd in cmd_excludes:
            continue
        if item['title'] == 'explainshell':
            ss = ' '
        cmds = ss.join(args[0:2])
        if item['title'] in ('die.net', 'Manpages') and cmd != 'git':
            cmds = cmd

        url = url.format(cmds)
        item['subtitle'] = url
        item['arg'] = url
        item['valid'] = True
        wf.add_item(**item)


    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))

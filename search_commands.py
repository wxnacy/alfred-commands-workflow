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

def get_all_commands():
    '''获取所有的命令'''
    files = os.listdir('./commands')
    commands = []
    for f in files:
        if f.endswith('.json'):
            filename = './commands/' + f
            data = read_json(filename)
            commands.extend(data)
    return commands

def main(wf):
    args = wf.args
    logging.info(args)

    commands = get_all_commands()
    input_cmd = ' '.join(args)
    for cmd in commands:
        if cmd['title'].startswith(input_cmd):
            cmd['valid'] = True
            cmd['arg'] = cmd['title']
            wf.add_item(**cmd)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))

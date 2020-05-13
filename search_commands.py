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

def read_csv(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    logging.info(lines)
    items = []
    for line in lines:
        ls = line.split(',')
        item = dict(title = ls[0].strip(" "), subtitle = ls[1].strip(" "))
        #  logging.info(item)
        items.append(item)

    return items

def get_all_commands():
    '''获取所有的命令'''
    files = os.listdir('./commands')
    commands = []
    for f in files:
        if f.endswith('.csv'):
            filename = './commands/' + f
            data = read_csv(filename)
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

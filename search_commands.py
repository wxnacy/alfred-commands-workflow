#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sys
import os
import logging
import timeit

from workflow import Workflow3
from common import read_cmd

ABBR = {
        "py": "python",
        "vg": "vagrant",
        }

def get_all_commands():
    '''获取所有的命令'''
    files = os.listdir('./commands')
    commands = []
    for f in files:
        if f.startswith('cmd_'):
            filename = './commands/' + f
            data = read_cmd(filename)
            commands.extend(data)
    return commands

def simple_search(wf, items, q):
    '''简单搜索'''
    like_lines = []
    split_likes = []
    cmds = q.split(" ", 1)
    cmd = cmds[0]
    args = cmds[1] if len(cmds) > 1 else ''
    for item in items:
        title = item['title']
        # 先完全匹配
        if title.startswith(q):
            wf.add_item(**item)
            continue
        # 再匹配前缀
        if title.startswith(cmd):
            split_likes.append(item)
            continue

        # 最后匹配包含
        if q in item['title']:
            like_lines.append(item)
            continue

    for item in split_likes:
        lines = item['title'].split(" ", 1)
        if len(lines) == 1:
            continue

        if args in lines[1]:
            wf.add_item(**item)


    for item in like_lines:
        wf.add_item(**item)

def main(wf):
    b = timeit.default_timer()
    args = wf.args
    logging.info(args)
    # 检查缩写
    for k, v in ABBR.items():
        if args[0] == k:
            args[0] = v

    commands = get_all_commands()

    input_cmd = ' '.join(args)
    simple_search(wf, commands, input_cmd)

    logging.info(timeit.default_timer() - b)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sys
import os
import logging
import timeit

from workflow import Workflow3

ABBR = {
        "py": "python",
        "vg": "vagrant",
        }

#  def read_json(filename):
    #  lines = []
    #  with open(filename, 'r') as f:
        #  lines = f.readlines()
    #  return json.loads(''.join(lines))

#  def read_csv(filename):
    #  lines = []
    #  with open(filename, 'r') as f:
        #  lines = f.readlines()
    #  logging.info(lines)
    #  items = []
    #  for line in lines:
        #  ls = line.split(',')
        #  item = dict(title = ls[0].strip(" "), subtitle = ls[1].strip(" "))
        #  items.append(item)
    #  return items

def read_file(filename):
    with open(filename, 'r') as f:
        return [o.strip('\n').strip(" ") for o in f.readlines()]

def read_cmd(filename):
    '''
    读取指令文件
    '''
    lines = read_file(filename)
    lines = list(filter(lambda x: x, lines))
    items = []
    num = len(lines) / 2
    # 设置 icon
    # 查找是否存在如下对应文件
    # ./commands/cmd_{category}
    # ./icon/{category}.png
    cmd_name = os.path.basename(filename).split("_")[1]
    icon = './icon.png'
    cmd_icon_path = './icon/{}.png'.format(cmd_name)
    if os.path.exists(cmd_icon_path):
        icon = cmd_icon_path
    for i in range(num):
        item = dict(
            title = lines[i * 2 + 1],
            subtitle = lines[i * 2],
            icon = icon,
            valid = True,
        )
        item['arg'] = item['title']
        items.append(item)
    return items


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

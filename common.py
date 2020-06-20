#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:
import os


def read_file(filename):
    '''读取文件，并返回列表'''
    with open(filename, 'r') as f:
        return [o.strip('\n').strip(" ") for o in f.readlines()]

def read_cmd(filename):
    '''
    读取指令文件
    '''
    lines = read_file(filename)
    lines = list(filter(lambda x: x, lines))
    items = []
    num = int(len(lines) / 2)
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

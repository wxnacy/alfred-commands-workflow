#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import os
import shutil
from common import read_cmd


YML = '''
site_name: 常用命令      # 站点名称
nav:                    # 文档目录
    - 首页: index.md
    {}
theme: readthedocs      # 主题
'''

SOURCE_DIR = 'commands'
OUTPUT_DIR = 'docs'

def cmd2md(filename):
    filepath = f'{SOURCE_DIR}/{filename}'
    outfile = f'{OUTPUT_DIR}/{fmt_name(filename)}.md'
    input_lines = read_cmd(filepath)
    outlines = []
    input_lines.sort(key = lambda x: x['title'])
    title_key = set()
    for line in input_lines:
        title = line['subtitle']
        cmd = line['title']
        cmd_begin = ' '.join(cmd.split(" ")[:2])
        if cmd_begin not in title_key:
            title_key.add(cmd_begin)
            outlines.append(f"## {cmd_begin}\n")

        title = f'**{title[2:]}**\n'
        cmd = f'```\n{cmd}\n```\n'

        outlines.append(title)
        outlines.append(cmd)
    with open(outfile, 'w') as out:
        out.writelines(outlines)

def fmt_name(name):
    return name[4:]

def first_upper(name):
    return name[0].upper() + name[1:]

def cmd2mdname(name):
    return fmt_name(name) + '.md'

def main(dirname):
    '''转换'''
    files = os.listdir(dirname)
    files.sort()
    navs = []
    for f in files:
        if not f.startswith('cmd_'):
            continue
        cmd2md(f)
        navs.append(f'- {first_upper(fmt_name(f))}: {fmt_name(f)}.md')

    #  shutil.move(f'{OUTPUT_DIR}/{cmd2mdname(files[0])}', f'{OUTPUT_DIR}/index.md')
    nav = '\n    '.join(navs)
    #  nav = nav.replace(cmd2mdname(files[0]), 'index.md')
    yml = YML.format(nav)
    with open('mkdocs.yml', 'w') as f:
        f.write(yml)






if __name__ == "__main__":
    main(SOURCE_DIR)

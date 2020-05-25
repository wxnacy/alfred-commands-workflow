#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sys
import json
import os
import logging
import subprocess

from workflow import Workflow3
from workflow import web

def run(cmd):
    '''运行 shell 命令'''
    cmds = cmd.split(" ")
    return subprocess.check_output(cmds).decode()

def get_local_ip():
    '''
    获取内网 ip
    '''
    lines = run("ifconfig").replace("\t", "").split("\n")
    is_local = 0
    for line in lines:
        if is_local and line.startswith("inet "):
            return line.split(" ")[1]
        if line.startswith("en0"):
            is_local = 1

def main(wf):
    args = wf.args
    logging.info(args)
    ip = args[0]

    if ip == "local":
        local_ip = get_local_ip()
        item = dict(arg = local_ip, valid = True, title = local_ip, subtitle = '内网 ip')
        wf.add_item(**item)
        wai_ip = run("curl ifconfig.io").replace("\n", "")
        item = dict(arg = wai_ip, valid = True, title = wai_ip, subtitle = '外网 ip')
        wf.add_item(**item)

    if len(ip.split(".")) == 4:
        url = "https://ipapi.co/{}/json".format(ip)
        res = web.get(url).json()
        logging.info(res)

        region = "{}, {}".format(res['country_name'], res['country_capital'])
        item = dict(arg = region, valid = True, title = region,
                subtitle = '国家，城市')
        wf.add_item(**item)

        latlng = "{},{}".format(res['latitude'], res['longitude'])
        item = dict(arg = latlng, valid = True, title = latlng,
                subtitle = '经纬度')
        wf.add_item(**item)

        latlng = "{} {}".format(res['timezone'], res['utc_offset'])
        item = dict(arg = latlng, valid = True, title = latlng,
                subtitle = '时区')
        wf.add_item(**item)

    logging.info(list(filter(lambda o: 'item' in o, dir(wf))))
    logging.info(wf._items)
    if not wf._items:
        wf.add_item(title="搜索 ip", subtitle = ip)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))

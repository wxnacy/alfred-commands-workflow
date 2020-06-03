#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sys
import json
import os
import logging
import subprocess
import re

from workflow import Workflow3
from workflow import web
import time
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from pytz import utc


def input_type(text):
    '''判断输入类型'''
    try:
        int(text)
        return int
    except ValueError:
        pass

    return str

def now():
    '''获取当前时间'''
    ts = int(time.time())
    return format_timestamp(ts)

def fmt_dt(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def format_timestamp(ts):
    '''格式化时间戳'''
    res = dict(timestamp = ts)
    t = datetime.fromtimestamp(ts)
    res['local'] = fmt_dt(t)
    t = datetime.utcfromtimestamp(ts)
    #  t = t.replace(tzinfo=utc)

    for i in list(range(-12, 13)):
        dt = t + timedelta(hours=i)
        res[i] = fmt_dt(dt)

    return res

def output_result(wf, res):
    '''格式化输出'''
    item = dict(valid = True)
    item['title'] = res['timestamp']
    item['subtitle'] = '时间戳'
    item['arg'] = item['title']
    wf.add_item(**item)

    for k, v in res.items():
        item['title'] = v
        if k == 'local':
            item['subtitle'] = '本地时间'
            item['arg'] = item['title']
            wf.add_item(**item)
        elif k == 0:
            item['subtitle'] = 'UTC 时间'
            item['arg'] = item['title']
            wf.add_item(**item)
        elif k == -4:
            item['subtitle'] = '纽约时间'
            item['arg'] = item['title']
            wf.add_item(**item)
        elif k == -7:
            item['subtitle'] = '太平洋时间'
            item['arg'] = item['title']
            wf.add_item(**item)

def unit2seconds(num, unit):
    seconds = 0
    if unit.startswith("year"):
        seconds = num * 365 * 24 * 60 * 60
    elif unit.startswith("month"):
        seconds = num * 30 * 24 * 60 * 60
    elif unit.startswith("day"):
        seconds = num * 24 * 60 * 60
    elif unit.startswith("hour"):
        seconds = num * 60 * 60
    elif unit.startswith("minute"):
        seconds = num * 60
    elif unit.startswith("second"):
        seconds = num 
    return seconds


def main(wf):
    args = wf.args
    logging.info(args)
    t = args[0]

    whole_input = ' '.join(args)
    # 获取单位时间之前的时间戳
    findres = re.findall('\d+ [days|minutes|seconds|month|years|hours]+ ago',
            whole_input)
    if findres:
        finds = findres[0].split(" ")
        num = int(finds[0])
        unit = finds[1]
        seconds = unit2seconds(num, unit)
        res = format_timestamp(int(time.time()) - seconds)
        output_result(wf, res)
        wf.send_feedback()
        return

    # 获取单位时间之后的时间戳
    findres = re.findall('\d+ next [days|minutes|seconds|month|years|hours]+',
            whole_input)
    if findres:
        finds = findres[0].split(" ")
        num = int(finds[0])
        unit = finds[2]
        seconds = unit2seconds(num, unit)
        res = format_timestamp(int(time.time()) + seconds)
        output_result(wf, res)
        wf.send_feedback()
        return


    type = input_type(t)
    if type == int:
        res = format_timestamp(int(t))
        output_result(wf, res)

    item = dict(valid = True)
    if t == 'now':
        res = format_timestamp(int(time.time()))
        #  res = now()
        output_result(wf, res)

    logging.info(list(filter(lambda o: 'item' in o, dir(wf))))
    logging.info(wf._items)
    if not wf._items:
        wf.add_item(title="输入需要转换的时间", subtitle = ' '.join(args))

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))


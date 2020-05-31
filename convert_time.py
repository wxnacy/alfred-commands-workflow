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
    #  t = datetime.fromtimestamp(ts)
    t = datetime.utcfromtimestamp(ts)
    res['local'] = fmt_dt(datetime.now())
    #  t = t.replace(tzinfo=timezone("UTC"))

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

def main(wf):
    args = wf.args
    logging.info(args)
    t = args[0]

    whole_input = ' '.join(args)

    type = input_type(t)
    if type == int:
        res = format_timestamp(int(t))
        output_result(wf, res)


    item = dict(valid = True)
    if t == 'now':
        res = now()
        output_result(wf, res)

    logging.info(list(filter(lambda o: 'item' in o, dir(wf))))
    logging.info(wf._items)
    if not wf._items:
        wf.add_item(title="输入需要转换的时间", subtitle = ' '.join(args))

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))


#!/usr/bin/env bash
# 部署指定tag 的api程序
# __author__ = "wenxiaoning(wenxiaoning@gochinatv.com)"
# __copyright__ = "Copyright of GoChinaTV (2017)."

MSG=$@
git add . && git commit -m "${MSG}"

#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

python convert.py
mkdocs build

for file in `find site | grep '\.'`
do
    outfile=`python -c "print('${file}'.replace('site/', ''))"`
    ossutil cp -u $file oss://cmd-cn/${outfile}
done

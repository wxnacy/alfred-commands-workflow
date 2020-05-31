#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

# result=`$@`

$@ | while read line
do
	echo $line
done

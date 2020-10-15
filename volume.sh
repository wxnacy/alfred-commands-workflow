#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

curr_vol=$(osascript -e 'output volume of (get volume settings)')

# echo $curr_vol
if [[ $1 == 'sub' && $curr_vol > 0 ]]
then
    curr_vol=$[ curr_vol - 10 ]
fi

if [[ $1 == 'add' ]]
then
    curr_vol=$[ curr_vol + 10 ]
fi

osascript -e "set volume output volume $curr_vol"
echo 'volume' $1 10 'success current' $curr_vol

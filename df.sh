#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

disk=`df -h | grep 'disk.*System'`
disks=(${disk})
VOLUME=$(system_profiler SPSoftwareDataType | grep 'Boot Volume' | awk '{print substr($0, index($0,$3))}')

subtitle="Size: ${disks[1]} Used: ${disks[2]} Avail: ${disks[3]}"

cat << EOB
<?xml version="1.0"?>
<items> 
<item uid="" arg="${subtitle}">
    <title>${VOLUME}</title>
    <subtitle>${subtitle}</subtitle>
    </item>
</items>
EOB

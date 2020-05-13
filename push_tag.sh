#!/usr/bin/env bash

TAG_NAME=$1
PUSH_MSG=${@/$1/}


main(){
    ./push.sh $PUSH_MSG
    git tag ${TAG_NAME}
    git push origin ${TAG_NAME}
}

if [ ! ${TAG_NAME} ]
then
    echo 'UAGE: ./push_tag.sh <regex:tag_name>'
else
    main
fi

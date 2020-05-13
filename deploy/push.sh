#!/usr/bin/env bash
# 部署指定tag 的api程序
# __author__ = "wenxiaoning(wenxiaoning@gochinatv.com)"
# __copyright__ = "Copyright of GoChinaTV (2017)."

MSG=$@
branch_name=`./deploy/get_branch.sh`

push(){
    echo '******************************'
    echo '********开始push api：'
    echo '******************************'
    ./deploy/commit.sh ${MSG}
    git pull origin $branch_name
    git add . && git commit -m "${MSG}"
    git push origin $branch_name
    echo '******************************'
    echo '********部署成功'
    echo '******************************'
}

main(){
    if [ ! "${MSG}" ]
    then
        echo 'UAGE: ./winn_push.sh <string:commit msg>'
    else
        push
    fi
}

main

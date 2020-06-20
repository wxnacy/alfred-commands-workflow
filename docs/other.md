## crontab -e
**编辑服务器定时任务**
```
crontab -e
```
## crontab -l
**查看服务器定时任务列表**
```
crontab -l
```
## df -h
**查看磁盘使用情况，并格式化输出**
```
df -h
```
## du -d
**查看第一层目录的文件夹大小，并格式化输出**
```
du -d 1 -h
```
## echo -n
**复制当前目录**
```
echo -n $(echo -n $(pwd) | sed 's/ /\\ /g') | pbcopy
```
**复制一段文字**
```
echo -n 'hello world' | pbcopy
```
## ifconfig |
**查看 Linux 系统内网 ip**
```
ifconfig | grep 'eth0' -A 1 | grep 'inet ' | awk '{print $2}' | sed 's/addr://g'
```
## pbpaste
**黏贴**
```
pbpaste
```
## ps -ef
**查看进程，并过滤关键字**
```
ps -ef | grep <pattern>
```

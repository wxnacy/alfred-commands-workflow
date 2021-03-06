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
## find .
**查找当前目录及子目录下所有文件**
```
find .
```
**查找当前目录及子目录下所有不是 .ipynb 后缀的文件**
```
find . ! -name "*.ipynb"
```
**查找当前目录及子目录下所有 .ipynb 后缀的文件，并忽略大小写**
```
find . -iname "*.ipynb"
```
**向下查找 1 层深度**
```
find . -maxdepth 1
```
**查找当前目录及子目录下所有 .ipynb 后缀的文件**
```
find . -name "*.ipynb"
```
**匹配文件路径或者文件**
```
find . -path "*ipynb*"
```
**基于正则表达式匹配文件路径**
```
find . -regex ".*ipynb"
```
**根据文件类型进行搜索**
```
find . -type f
```
**搜索大于 1k 的文件**
```
find . -type f -size +1k
```
**搜索小于 100k 的文件**
```
find . -type f -size -100k
```
**搜索等于 100k 的文件**
```
find . -type f -size 100k
```
## find ..
**查找上层目录并多匹配**
```
find .. -name "*.py" -o -name "*.pdf"
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

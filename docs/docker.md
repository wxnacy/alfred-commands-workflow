## docker --version
**查看版本**
```
docker --version
```
## docker build
**在当前目录创建镜像，不使用缓存**
```
docker build --no-cache -t <image-name> .
```
**在当前目录创建镜像**
```
docker build -t <image-name> .
```
## docker container
**重启容器**
```
docker container restart <continer-name>
```
## docker exec
**在交互模式下进入容器，并进入 bash 环境**
```
docker exec -it <continer-name> /bin/bash
```
## docker image
**查看镜像列表**
```
docker image ls
```
## docker info
**查看 docker 详情**
```
docker info
```
## docker logs
**从最后 10 行开始实时查看日志**
```
docker logs -f --tail 10 <continer-name>
```
**从最后 10 行开始实时查看日志并过滤信息**
```
docker logs -f --tail 10 <continer-name> 2>&1 | grep <pattern>
```
## docker ps
**查看当前运行的进程列表**
```
docker ps
```
**查看所有进程列表**
```
docker ps -a
```
## docker restart
**重启所有服务**
```
docker restart `docker ps -a | awk '{print $1}'`
```
## docker version
**分别查看 client 和 server 的版本**
```
docker version
```
## docker-compose up
**重新创建容器，并在后台运行**
```
docker-compose up --force-recreate -d <name>
```

## vagrant box
**查看所有 box 列表**
```
vagrant box list
```
**删除 box**
```
vagrant box remove <box-name>
```
**删除 box，并指定版本**
```
vagrant box remove <box-name> --box-version <version>
```
**更新 box 版本"**
```
vagrant box update
```
**更新指定 box 版本**
```
vagrant box update --box <box-name>
```
## vagrant destroy
**销毁虚拟机，并对询问回答 yes"**
```
vagrant destroy -f
```
**销毁虚拟机"**
```
vagrant destroy [name|id]
```
## vagrant global-status
**查看所有虚拟机状态**
```
vagrant global-status
```
## vagrant halt
**登陆虚拟机"**
```
vagrant halt
```
## vagrant init
**在当前文件夹初始化 Vagrantfile**
```
vagrant init [name [url]]
```
**在当前文件夹初始化 centos7**
```
vagrant init centos/7
```
## vagrant package
**打包 box"**
```
vagrant package
```
**打包 box，并指定包名"**
```
vagrant package --ouput <box-name>
```
## vagrant reload
**重新加载虚拟机配置**
```
vagrant reload
```
## vagrant ssh
**登陆虚拟机"**
```
vagrant ssh
```
## vagrant status
**当前虚拟机状态**
```
vagrant status
```
## vagrant up
**启动虚拟机"**
```
vagrant up
```

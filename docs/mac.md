## /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan
**扫描附近可用 Wifi热点**
```
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan
```
## defaults write
**在文件夹不显示隐藏文件**
```
defaults write com.apple.finder AppleShowAllFiles no; killall Finder /System/Library/CoreServices/Finder.app
```
**在文件夹显示隐藏文件**
```
defaults write com.apple.finder AppleShowAllFiles yes; killall Finder /System/Library/CoreServices/Finder.app
```
## dscacheutil -flushcache
**清空DNS缓存**
```
dscacheutil -flushcache
```
## ifconfig |
**查看 Mac 系统内网 ip**
```
ifconfig | grep en0 -A 3 | grep 'inet ' | awk '{print $2}'
```
## networksetup -listallnetworkservices
**列出本机所有网络服务**
```
networksetup -listallnetworkservices
```
## networksetup -setairportnetwork
**加入 WIFI**
```
networksetup -setairportnetwork en0 <wifiname> <wifipsword>
```
## networksetup -setairportpower
**关闭 Wifi**
```
networksetup -setairportpower en0 off
```
**启动 WIFI**
```
networksetup -setairportpower en0 on
```
## system_profiler SPSoftwareDataType
**系统软件总览**
```
system_profiler SPSoftwareDataType
```

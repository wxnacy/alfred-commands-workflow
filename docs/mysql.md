## select *
**查看正在执行的线程，并按 Time 倒排序，看看有没有执行时间特别长的线程**
```
select * from information_schema.processlist where Command != 'Sleep' order by Time desc;
```
**查询 processlist**
```
select * from information_schema.processlist;
```
## select client_ip,count(client_ip)
**按客户端 IP 分组，看哪个客户端的链接数最多**
```
select client_ip,count(client_ip) as client_num from (select substring_index(host,':' ,1) as client_ip from information_schema.processlist ) as connect_info group by client_ip order by client_num desc;
```
## select concat('kill
**找出所有执行时间超过 5 分钟的线程，拼凑出 kill 语句**
```
select concat('kill ', id, ';') from information_schema.processlist where Command != 'Sleep' and Time > 300 order by Time desc;
```
## show processlist;
**查询 processlist**
```
show processlist;
```

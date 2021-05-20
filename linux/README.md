# The manual of Linux

面向Linux的基本教程。

## 说明

以下操作均在 elementary OS 5.0 下调试通过。

## util

下面是一些我认为值得推荐的软件。

|软件名|简介|
|:--:|:--:|
|[bat](https://github.com/sharkdp/bat)|更好的cat|
|[cloc](https://github.com/AlDanial/cloc)|统计代码行数|
|[htop](https://github.com/htop-dev/htop)|更好的top|
|[screenfetch](https://github.com/KittyKatt/screenFetch)|显示系统信息|
|[tldr](https://github.com/tldr-pages/tldr)|直观地展示一个命令的常见用法|
|[viu](https://github.com/atanunq/viu)|在终端显示图片|

每分钟记录一次内存使用情况。

```
# 创建 cmds.cron 文件并添加以下内容：
* * * * * /bin/date +"\%F \%T" >> ~/mem.txt && /usr/bin/free -h >> ~/mem.txt

# 加入到 cron 中
$ crontab cmds.cron
```

通过 alias 设置命令的别名。

```
$ echo "alias psx='ps -ef|grep -v grep|grep'" >> $HOME/.bashrc
$ source $HOME/.bashrc
```

通过 nohup 将进程以忽略挂起信号的方式运行。

```
# 准备 main.py 文件
$ echo -e "import time\nwhile True: print(int(time.time()), flush=True); time.sleep(1)" > main.py

# 不重定向 stdin 的情况下，终端退出后进程也随之退出
$ python3 main.py &

# 进程不受终端退出的影响
$ nohup python3 main.py &
```

通过以下命令查看 JSON 文件。

```
$ echo '{ "name": "paoqi" }' > who.json

$ sudo apt install jq
$ jq < who.json

$ python3 -m json.tool who.json
```

查看不同优化级别的汇编代码。

```
$ echo "int main() { int m[10] = {0}; return 0; }" > main.cpp
$ g++ -O0 -S main.cpp -o main.s
$ g++ -O2 -S main.cpp -o main.S
```

产生并调试 core 文件。

```
$ echo "int main() { char *p = nullptr; *p = 'c'; }" > main.cpp
$ g++ main.cpp -o app

$ ulimit -c unlimited
$ ./app
$ gdb app core

(gdb) bt
```

通过 find 命令进行一些操作。

```
# 在 /usr/include 目录及其子目录中搜索包含 IPPROTO_TCP 的行
$ find /usr/include -name *.h|xargs grep -n --color IPPROTO_TCP

# 统计 pqnet 目录下 C++ 代码的行数（不包括空行）
$ find pqnet -regex '.*\.\(cpp\|h\)' -type f|xargs cat|grep -v ^$|wc -l
$ find pqnet -regextype posix-extended -regex '.*.(cpp|h)' -type f|xargs cat|grep -v ^$|wc -l

# 查找大于500KB且小于10MB的文件
$ find /bin -size +500k -size -10M -type f -exec ls -lh {} \;

# 查找最近30天内被访问过的文件
$ find /usr/local/bin -atime -30 -type f -exec stat -c "%x %n" {} \;

# 查找 pqnet 目录及其子目录下的 cpp 文件，但不包括 tests 目录
$ find pqnet -path */tests -prune -o -name '*.cpp' -print
$ find pqnet -name '*.cpp' -not -path '*/tests/*'
```

通过 grep 命令进行一些操作。

```
$ cat /proc/cgroups|grep -e cpu -e net
$ cat /proc/cgroups|grep -E 'cpu|net'

# egrep(/bin/egrep) == grep -E "$@"
# fgrep(/bin/fgrep) == grep -F "$@"
$ pgrep -fal ssh
```

操作用户/组。

```
# 创建组/用户
$ groupadd team
$ useradd -m -g team -s /bin/bash pq

# 将用户添加到指定组
$ usermod -aG team pq
$ gpasswd -a pq team
# 将用户从指定组删除
$ gpasswd -d pq team

# 修改组名
$ groupmod -n teamX team

# 删除用户/组
$ userdel -r pq
$ groupdel teamX
```

其他的一些命令放在这里。

```
# 清空 xxx.txt 文件
$ cat /dev/null > xxx.txt
# 查看 meminfo 文件最后10行的内容
$ tail -n 10 /proc/meminfo

# 为 redis-cli 建立软链接
$ ln -snf /usr/local/redis/bin/redis-cli rdc

# 打印 "123456" 的 base64 值
$ echo -n "123456"|base64
# 打印 bash 的 MD5 值
$ md5sum /bin/bash
# 打印 bash 的 SHA1 值
$ sha1sum /bin/bash
# 打印 bash 的校验和及文件所占用的磁盘块数
$ sum /bin/bash
# 打印 bash 的 CRC 值及文件大小的字节数
$ cksum /bin/bash

# 按单字节输出来自 stdin 的数据
$ echo "123456"|od -c
# 随机生成长度为13个字符的密码
$ echo $(cat /dev/urandom|tr -cd a-zA-Z0-9|head -c 13)

# 查看 /bin/bash 的文件头信息
$ readelf -h /bin/bash
$ objdump -f /bin/bash
# 对 app.out 进行反汇编
$ objdump -ld app.out

# 将给定地址翻译为对应行
$ addr2line -fe app.out addr1 addr2

# 忽略重复的行
$ echo -e 'Hello!\nHello!\nHi'|uniq

# 查看用户
$ cat /etc/passwd
# 查看存储用户密码信息的文件
$ cat /etc/shadow
# 查看组
$ cat /etc/group
# 查看组加密信息
$ cat /etc/gshadow

# 查看 sudo 的权限控制情况
$ cat /etc/sudoers
# 查看用于设置用户限制的文件
$ cat /etc/login.defs

# 查看当前工作目录
$ pwd
# 查看当前登录的用户名
$ whoami

# 显示系统当前登录的所有用户名
$ users
# 查看有谁登录在上面
$ who -Hu
# T掉指定用户
$ pkill -t your-tty

# 显示用户的 ID 及所属用户组的ID
$ id your-user
# 显示用户所属的组
$ groups your-user

# 切换到其他用户组（用户隶属2个或以上的组）
$ newgrp your-group
# 以指定组 ID 执行命令（应为用户所属的组）
$ sg your-group -c your-command

# 打印当前主机的数字化标识
$ hostid
# 显示主机名
$ hostname
```

## monitor

查看系统。

```
# 查看 cpu 相关参数
$ lscpu
# 查看 processor 的数量
$ cat /proc/cpuinfo|grep processor|wc -l

# 显示内核模块的状态信息
$ sh -c lsmod
# 查看内核参数
$ sysctl -a

# 查看资源限制情况
$ ulimit -a

# 查看消息队列、共享内存及信号量的信息
$ ipcs

# 打印内核信息
$ uname -a
# 查看发行版信息
$ cat /etc/issue
# 获取系统位数
$ getconf LONG_BIT

# 查看系统负载
$ w
$ uptime
$ cat /proc/loadavg

# 查看系统总共运行了多长时间
$ uptime -p
$ cat /proc/uptime

# 查看 mounts 文件第10到20行的内容（没有'+'就是第11行）
$ cat -n /proc/mounts|head -n 20|tail -n +10
```

查看磁盘。

```
# 查看文件系统的磁盘使用情况
$ df -h

# 查看当前目录下所有文件及文件夹的大小
$ du -sh ./*

# 显示文件或目录的信息
$ stat ~/.profile

# 了解s及t特殊权限位，g+s在此并未列出
$ stat /usr/bin/passwd # u+s
$ stat /tmp            # o+t
```

查看进程。

```
# 查看对应进程的文件打开情况
$ lsof -p your-pid

# 查看前10个占用内存最多的进程
$ ps aux|sort -k6nr|head -n 10

# 查看引用的so文件
$ ldd /usr/local/bin/lua

# 查看符号表
$ nm -A /usr/local/lib/liblua.a

# 跟踪系统调用
$ strace -ttT cat /proc/uptime

# 1s获取一次进程状态
$ top -d 1
# 以批处理模式获取一次进程状态
$ top -bc -w 512 -n 1

# 调用 bash 内置的 time 命令测量耗时
$ time ps -ef
# 调用 /usr/bin/time 测量耗时
$ \time -v ps -ef
$ /usr/bin/time -v ps -ef

# 查看进程的内存映射关系
$ sudo pmap -dp your-pid

$ sysdig -cl
$ sudo sysdig -c topprocs_cpu   # Top processes by CPU usage
$ sudo sysdig -c topfiles_bytes # Top files by R+W bytes
```

## netdev

默认没有的话请通过包管理器安装。

```
$ sudo apt install net-tools
```

使用一些功能时 ~~net-tools~~ 和 iproute2 对应的命令如下表所示：

|说明|net-tools|iproute2|
|--|--|--|
|查看网络接口的状态|ifconfig|ip link<br>ip addr|
|查看统计信息|ifconfig -s<br>netstat -i|ip -s link|
|查看ARP表|arp -a<br>arp -an<br>arp -e<br>arp -en|ip neigh|
|查看路由表|route<br>route -n<br>netstat -r<br>netstat -rn|ip route|
|查看TCP/UDP监听端口的状态|netstat -tul<br>netstat -tunl|ss -tul<br>ss -tunl|
|查看多播地址|ipmaddr<br>netstat -g|ip maddr|

通过 iptables 控制端口开放情况。

```
# 查看规则
$ sudo iptables -L -n
# 禁用8080端口
$ sudo iptables -A INPUT -p tcp --dport 8080 -j DROP
# 解除限制
$ sudo iptables -D INPUT -p tcp --dport 8080 -j DROP
```

通过 telnet 测试端口的连通性。

```
# 可用
$ telnet 220.181.38.148 80
# 大概率不可用
$ telnet 220.181.38.148 12358
```

通过 tcpdump 抓包。

```
$ sudo tcpdump -i lo tcp port 12358
```

通过 iperf 测试网络性能。

```
# 启动服务端
$ iperf -s 127.0.0.1
# 启动客户端
$ iperf -c 127.0.0.1
```

其他与网络相关的一些命令放在这里。

```
# 查看hosts
$ cat /etc/hosts
# 查看 DNS 配置
$ cat /etc/resolv.conf

# 查看 TCP 连接
$ ss -ta
$ lsof -i tcp

# 查询DNS
$ host baidu.com
$ nslookup baidu.com
$ dig baidu.com
```

## remotedev

默认没有的话请通过包管理器安装。

```
$ sudo apt install openssh-server
```

在 /etc/ssh/sshd_config 文件中启用以下配置：

```
# See sshd_config(5).

# 更换端口
Port port

# 如果ClientAliveInterval设置为15，ClientAliveCountMax设置为3，
# 那么45s后将断开与 无响应的SSH客户端 之间的连接
ClientAliveInterval 60
ClientAliveCountMax 3
```

配置 SSH 免密码登录。

```
$ ssh-keygen -t rsa

# Windows下可使用 Git Bash 进行操作
$ ssh-copy-id -i ~/.ssh/id_rsa_aliyun.pub user@host
```

创建 ~/.ssh/config 文件并添加以下内容：

```
# See ssh_config(5).
Host aliyun
HostName host
Port port
IdentityFile ~/.ssh/id_rsa_aliyun
User user
```

通过 scp 或其他命令上传/下载文件。

```
$ scp localfile user@host:remotefile
$ scp user@host:remotefile localfile

$ sftp user@host
sftp> help
# 获取远端文件列表
sftp> ls
# 获取本地文件列表
sftp> lls
sftp> get remotefile
sftp> put localfile
```

通过 openssl 命令进行一些操作。

```
# 生成1024位的私钥，用 AES-128-CBC 加密它，设置密码为123456，输出到 id_rsa.pri 文件
$ openssl genrsa -out id_rsa.pri -passout pass:123456 -aes-128-cbc 2048
# 从 id_rsa.pri 文件读取私钥，用密码123456解密，生成的公钥输出到 id_rsa.pub 文件
$ openssl rsa -in id_rsa.pri -passin pass:123456 -pubout -out id_rsa.pub

$ echo "Hi, Trump." > letter_lihua.txt
# 用公钥加密 letter_lihua.txt 文件，输出到 letter.pkg 文件
$ openssl rsautl -encrypt -pubin -inkey id_rsa.pub -in letter_lihua.txt -out letter.pkg
# 用私钥解密 letter.pkg 文件，输出到 letter_trump.txt 文件
$ openssl rsautl -decrypt -inkey id_rsa.pri -in letter.pkg -out letter_trump.txt

$ echo "Hello World!" > letter_python.txt
# 用私钥给 letter_python.txt 文件签名，输出到 letter.xyz 文件
$ openssl rsautl -sign -inkey id_rsa.pri -in letter_python.txt -out letter.xyz
# 用公钥验证 letter.xyz 文件的签名，输出到 letter_c.txt 文件
$ openssl rsautl -verify -pubin -inkey id_rsa.pub -in letter.xyz -out letter_c.txt
```

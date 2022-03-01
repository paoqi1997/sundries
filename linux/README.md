# The manual of Linux

面向 Linux 的基本教程。

## 说明

以下操作均在 elementary OS 5.0 下调试通过。

## recommendations

下面是一些我认为值得推荐的软件。

|软件名|主要编程语言|用途|
|:--:|:--:|:--:|
|[bat](https://github.com/sharkdp/bat)|Rust|更好的cat|
|[cloc](https://github.com/AlDanial/cloc)|Perl|统计代码行数|
|[dust](https://github.com/bootandy/dust)|Rust|更好的du|
|[fd](https://github.com/sharkdp/fd)|Rust|更好的find|
|[htop](https://github.com/htop-dev/htop)|C|更好的top|
|[lnav](https://github.com/tstack/lnav)|C++|高亮显示日志行|
|[screenfetch](https://github.com/KittyKatt/screenFetch)|Shell|显示系统信息|
|[tldr](https://github.com/tldr-pages/tldr)|Markdown|直观地展示一个命令的常见用法|
|[viu](https://github.com/atanunq/viu)|Rust|在终端显示图片|

## util

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

利用 valgrind 的 callgrind 工具分析程序中各个调用的耗时情况。

```
# 假定生成的文件是 callgrind.out.17440
$ valgrind --tool=callgrind ./httpserver

$ pip3 install gprof2dot

$ gprof2dot -f callgrind -n 0.8 -s callgrind.out.17440 > callgrind.dot

$ dot -Tpng callgrind.dot -o callgrind.png
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
$ g++ -g main.cpp -o app

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

# 在当前目录及其子目录中搜索包含 coroutine 的行，但不包括 .git 和 doc 目录
$ find . \( -path './.git' -o -path './doc' \) -prune -o -type f -print|xargs grep -in --color coroutine
```

通过 grep 命令进行一些操作。

```
$ cat /proc/cgroups|grep -e cpu -e net
$ cat /proc/cgroups|grep -E 'cpu|net'

# egrep(/bin/egrep) == grep -E "$@"
# fgrep(/bin/fgrep) == grep -F "$@"
$ pgrep -fal ssh
```

通过 sed 命令进行一些操作。

```
$ cat /proc/version > version.txt

# 删掉包含 GNU 内容的行
$ sed -i '/gnu/Id' version.txt
```

通过 awk 命令进行一些操作。

```
# 查看包含 python 进程的 PID 及 CMD
$ ps aux|grep python|grep -v grep|awk '{print $2,$11,$12}'
$ ps aux|grep python|grep -v grep|awk '{ s=$11; for(i=12;i<=NF;++i){ s=s" "$i }; print $2" "s }'
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

# 一边跟踪命令输出一边将其记录到文件中
$ ping bilibili.com|tee ping.log

# 比较文件差异
$ diff -u /etc/apt/sources.list.bak /etc/apt/sources.list|colordiff
$ colordiff -u /etc/apt/sources.list.bak /etc/apt/sources.list
$ vim -d /etc/apt/sources.list.bak /etc/apt/sources.list
$ vimdiff /etc/apt/sources.list.bak /etc/apt/sources.list

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

# 查看最近10条用户登入的记录
$ last -n 10
# 查看最近10条用户登入失败的记录
$ sudo lastb -n 10

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

# 查看 CPU 型号
$ cat /proc/cpuinfo|grep name|cut -d: -f2|uniq -c
# 查看物理 CPU 的数量（主板插槽上有多少个 CPU）
$ cat /proc/cpuinfo|grep 'physical id'|sort -u|wc -l
# 查看每个物理 CPU 中核的数量（一颗 CPU 的物理核数）
$ cat /proc/cpuinfo|grep 'cpu cores'
$ cat /proc/cpuinfo|grep 'core id'|sort -u|wc -l
# 查看逻辑 CPU 的数量（逻辑核总数）
$ cat /proc/cpuinfo|grep processor|sort -u|wc -l

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

$ sudo apt install lsb-core
# 打印 LSB 和特定于发行版的信息
$ lsb_release -a

# 查看系统负载
$ w
$ uptime
$ cat /proc/loadavg

# 查看系统总共运行了多长时间
$ uptime -p
$ cat /proc/uptime

# 查看 mounts 文件第10到20行的内容（没有'+'就是最后10行内容）
$ cat -n /proc/mounts|head -n 20|tail -n +10

# Display or control the kernel ring buffer.
$ dmesg -H
# Query the journal.
$ journalctl -r
```

查看磁盘。

```
# 查看文件系统的磁盘使用情况
$ df -h

# 查看当前目录的总大小
$ du -sh .
$ du -ahd 0 .
# 查看当前目录下所有文件及文件夹的大小
$ du -sh *
$ du -ahd 0 *
$ du -ahd 1 .

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

# 查看引用的 so 文件
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

使用 tcptrack 跟踪 TCP 连接。

```
$ tcptrack -i eth0 port 80
```

使用 iperf 或 netperf 测试网络性能。

```
# 启动服务端
$ iperf -s -p 9307
# 启动客户端
$ iperf -c 127.0.0.1 -p 9307

# 启动服务端
$ sudo netserver -4 -p 7751
# 启动客户端
$ netperf -p 7751 -l 3
```

其他与网络相关的一些命令放在这里。

```
# 查看 hosts
$ cat /etc/hosts
# 查看 DNS 配置
$ cat /etc/resolv.conf

# 查看 TCP 连接
$ ss -ta
$ lsof -i tcp

# 查看打开的 TCP 连接对应的 PID
$ sudo ss -tnpl
# 查看[1, 1024]端口范围内打开的 TCP 连接
$ sudo lsof -iTCP:1-1024 -sTCP:LISTEN -n -P

# 查询 DNS
$ host baidu.com
$ nslookup baidu.com
$ dig baidu.com

# 查看去 baidu.com 的路上经过了哪些自治系统（Autonomous System, AS）
$ mtr -z baidu.com
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

# 如果 ClientAliveInterval 设置为15，ClientAliveCountMax 设置为3，
# 那么45s后将断开与 无响应的 SSH 客户端 之间的连接
ClientAliveInterval 60
ClientAliveCountMax 3
```

配置 SSH 免密码登录。

```
$ ssh-keygen -t rsa

# Windows 下可使用 Git Bash 进行操作
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

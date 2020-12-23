# The manual of Linux

面向Linux的基本教程。

## 说明

以下操作均在 elementary OS 5.0 下调试通过。

## mirror

将默认软件镜像换成中科大的镜像：

```
$ sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
$ sudo sed -i 's/cn.archive.ubuntu.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list
$ sudo sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list
$ sudo sed -i 's/http/https/' /etc/apt/sources.list
```

针对elementary.list的操作：

```
$ sudo cp /etc/apt/sources.list.d/elementary.list /etc/apt/sources.list.d/elementary.list.bak
$ sudo sed -i 's/ppa.launchpad.net/launchpad.proxy.ustclug.org/' /etc/apt/sources.list.d/elementary.list
$ sudo sed -i 's/http/https/' /etc/apt/sources.list.d/elementary.list
```

针对patches.list的操作：

```
$ sudo cp /etc/apt/sources.list.d/patches.list /etc/apt/sources.list.d/patches.list.bak
$ sudo sed -i 's/ppa.launchpad.net/launchpad.proxy.ustclug.org/' /etc/apt/sources.list.d/patches.list
$ sudo sed -i 's/http/https/' /etc/apt/sources.list.d/patches.list
```

## util

下面是一些我认为值得推荐的软件。

|软件名|简介|
|:--:|:--:|
|[bat](https://github.com/sharkdp/bat)|更好的cat|
|[screenfetch](https://github.com/KittyKatt/screenFetch)|展示系统信息|
|[tldr](https://github.com/tldr-pages/tldr)|更友好的man|
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
$ echo "alias psx='ps -ef|grep'" >> $HOME/.bashrc
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
$ sudo apt install jq
$ jq < xxx.json

$ python3 -m json.tool xxx.json
```

其他的一些命令放在这里。

```
# 在 /usr/include 目录及其子目录中搜索包含 IPPROTO_TCP 的行
$ find /usr/include -name *.h|xargs grep -n IPPROTO_TCP

# 查看 meminfo 文件的最后10行内容
$ tail -n 10 /proc/meminfo
# 清空 xxx.txt 文件
$ cat /dev/null > xxx.txt

# 打印 "123456" 的 base64 值
$ echo -n "123456"|base64
# 打印 bash 的 MD5 值
$ md5sum /bin/bash

# 按单字节输出来自 stdin 的数据
$ echo "123456"|od -c
# 随机生成长度为13个字符的密码
$ echo $(cat /dev/urandom|tr -cd a-zA-Z0-9|head -c 13)

# 查看组
$ cat /etc/group
# 查看组加密信息
$ cat /etc/gshadow
# 查看用户
$ cat /etc/passwd
# 查看存储用户密码信息的文件
$ cat /etc/shadow

# 查看 sudo 的权限控制情况
$ cat /etc/sudoers
# 查看用于设置用户限制的文件
$ cat /etc/login.defs

# 查看当前工作目录
$ pwd
# 查看当前登录的用户
$ whoami
```

## monitor

查看系统。

```
# 查看 cpu 相关参数
$ lscpu

# 查看 processor 的数量
$ cat /proc/cpuinfo|grep processor|wc -l

# 查看资源限制情况
$ ulimit -a

# 查看消息队列、共享内存及信号量的信息
$ ipcs

# 打印系统信息
$ uname -a
```

查看进程。

```
# 查看对应进程的文件打开情况
$ lsof -p your-pid

# 查看前10个占用内存最多的进程
$ ps aux|sort -k4nr|head -n 10

# 查看引用的so文件
$ ldd /usr/local/bin/lua

# 查看符号表
$ nm -A /usr/local/lib/liblua.a

# 跟踪系统调用
$ strace -ttT cat /proc/uptime
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

## 非apt/yum方式安装软件

能不用包管理器就不用包管理器。

### [Apache HTTP Server](https://httpd.apache.org)

提取相应的包。

```
$ tar -xzvf httpd-2.4.46.tar.gz

$ tar -C httpd-2.4.46/srclib -xzvf apr-1.7.0.tar.gz
$ mv httpd-2.4.46/srclib/apr-1.7.0 httpd-2.4.46/srclib/apr

$ tar -C httpd-2.4.46/srclib -xzvf apr-util-1.6.1.tar.gz
$ mv httpd-2.4.46/srclib/apr-util-1.6.1 httpd-2.4.46/srclib/apr-util

$ cd httpd-2.4.46
$ ./configure
$ make
$ sudo make install
```

### [Boost](https://www.boost.org/users/download/)

提取相应的包。

```
$ tar -xzvf boost_1_72_0.tar.gz
$ cd boost_1_72_0
$ ./bootstrap.sh --show-libraries

$ sudo ./b2 install     \
   --with-coroutine     \
   --with-date_time     \
   --with-regex         \
   --with-serialization \
   --with-system        \
   --with-thread

$ sudo ldconfig
```

### [CMake](https://cmake.org/download/)

提取相应的包。

```
$ tar -xzvf cmake-3.15.3.tar.gz
$ cd cmake-3.15.3
$ ./bootstrap
$ make
$ sudo make install
```

### [Golang](https://golang.google.cn/doc/install)

提取相应的包。

```
$ sudo tar -C /usr/local -xzvf go1.14.9.linux-amd64.tar.gz
```

添加 bin 到环境变量。

```
$ echo "export PATH=$PATH:/usr/local/go/bin" >> $HOME/.profile
$ source $HOME/.profile
```

设置[代理](https://goproxy.cn)。

```
# 开启模块支持
$ go env -w GO111MODULE=on
$ go env -w GOPROXY=https://goproxy.cn,direct
```

### [libevent](https://libevent.org)

提取相应的包。

```
$ tar -xzvf libevent-2.1.11-stable.tar.gz
$ cd libevent-2.1.11-stable
$ ./configure
$ make
$ sudo make install
$ sudo ldconfig
```

### [MariaDB](https://mariadb.com/kb/en/library/installing-mariadb-binary-tarballs/)

在root模式下执行以下命令。

```
$ groupadd mysql
$ useradd -g mysql mysql

$ tar -C /usr/local -xzvf mariadb-10.3.22-linux-x86_64.tar.gz

$ mv /usr/local/mariadb-10.3.22-linux-x86_64 /usr/local/mysql

$ cd /usr/local/mysql
$ ./scripts/mysql_install_db --user=mysql

$ chown -R root .
$ chown -R mysql data

$ ./bin/mysqld_safe --user=mysql &
```

在~/.profile文件中添加以下命令。

```
export PATH=$PATH:/usr/local/mysql/bin
```

运行一下。

```
$ source ~/.profile
```

设置开机自启。

```
$ cp support-files/mysql.server /etc/init.d/mysql
$ update-rc.d mysql defaults
```

设置密码。

```
$ mysqladmin -uroot password 123456
```

允许远程连接。

```sql
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
```

删除匿名用户。

```sql
MariaDB [(none)]> USE mysql;

MariaDB [mysql]> DELETE FROM user WHERE User = '';
MariaDB [mysql]> FLUSH PRIVILEGES;
```

### [MongoDB](https://www.mongodb.org/dl/linux/x86_64-ubuntu1804)

提取相应的包。

```
$ tar -C /usr/local -xzvf mongodb-linux-x86_64-ubuntu1804-4.2.3.tgz

$ mv /usr/local/mongodb-linux-x86_64-ubuntu1804-4.2.3 /usr/local/mongodb

$ cd /usr/local/mongodb
$ mkdir -p data/db
$ mkdir log
```

创建 mongod.conf 文件并添加以下内容：

```yaml
processManagement:
  fork: true
security:
  authorization: enabled
storage:
  dbPath: /usr/local/mongodb/data/db
systemLog:
  destination: file
  path: /usr/local/mongodb/log/mongod.log
```

在~/.profile文件中添加以下命令。

```
export PATH=$PATH:/usr/local/mongodb/bin
```

运行一下。

```
$ source ~/.profile
```

创建 /etc/systemd/system/mongodb.service 文件并添加以下内容：

```
[Unit]
Description=mongodb
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/mongodb/bin/mongod -f /usr/local/mongodb/mongod.conf
ExecStop=/usr/local/mongodb/bin/mongod --shutdown -f /usr/local/mongodb/mongod.conf
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

执行以下命令：

```
$ sudo systemctl enable mongodb
$ sudo systemctl start mongodb
```

创建用户。

```sql
> use admin
> db.createUser({
    user: "root",
    pwd: "123456",
    roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
})
> db.auth("root", "123456")
> db.getUser("root")
```

### [MySQL](https://dev.mysql.com/doc/refman/8.0/en/binary-installation.html)

在root模式下执行以下命令。

```
$ groupadd mysql
$ useradd -r -g mysql -s /bin/false mysql

$ tar -C /usr/local -xvf mysql-8.0.19-linux-glibc2.12-x86_64.tar.xz

$ mv /usr/local/mysql-8.0.19-linux-glibc2.12-x86_64 /usr/local/mysql

$ cd /usr/local/mysql
$ mkdir mysql-files
$ chown mysql:mysql mysql-files
$ chmod 750 mysql-files

# for log_error
$ mkdir log
$ touch log/mysqld.err
$ chown mysql log/mysqld.err
# for pid_file
$ mkdir /var/run/mysqld
$ chown mysql /var/run/mysqld

# Please remember your temporary password.
$ bin/mysqld --initialize --user=mysql

$ bin/mysql_ssl_rsa_setup
$ bin/mysqld_safe --user=mysql &
```

mysqld依赖[libaio1](https://pkgs.org/download/libaio1)，如果没有的话请通过包管理器安装：

```
$ sudo apt install libaio1
```

在~/.profile文件中添加以下命令。

```
export PATH=$PATH:/usr/local/mysql/bin
```

运行一下。

```
$ source ~/.profile
```

设置开机自启。

```
$ cp support-files/mysql.server /etc/init.d/mysql
$ update-rc.d mysql defaults
```

修改密码。

```
# Need to enter your temporary password.
$ mysqladmin -uroot -p password 123456
```

允许远程连接。

```sql
mysql> CREATE USER 'root'@'%' IDENTIFIED BY '123456';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
```

按 MySQL 8 之前的加密规则再次修改密码。

```sql
mysql> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
```

### [OpenJDK](https://jdk.java.net/archive/)

提取相应的包。

```
$ sudo tar -C /usr/local -xzvf openjdk-11.0.1_linux-x64_bin.tar.gz

$ sudo mv /usr/local/jdk-11.0.1 /usr/local/java
```

在$HOME/.profile文件中添加以下命令。

```
export PATH=$PATH:/usr/local/java/bin
```

运行一下。

```
$ source $HOME/.profile
```

### [OpenSSL](https://www.openssl.org/source/)

提取相应的包。

```
$ tar -xzvf openssl-1.1.1d.tar.gz
$ cd openssl-1.1.1d
$ ./config zlib --debug --prefix=/usr/local/openssl
$ make
$ sudo make install
```

### [protobuf](https://github.com/protocolbuffers/protobuf)

提取相应的包。

```
$ tar -xzvf protobuf-cpp-3.11.4.tar.gz
$ cd protobuf-3.11.4
$ ./configure
$ make
$ make check
$ sudo make install
$ sudo ldconfig
```

### [Redis](https://redis.io/download)

提取相应的包。

```
$ tar -xzvf redis-5.0.7.tar.gz
$ cd redis-5.0.7
$ make
$ sudo make install PREFIX=/usr/local/redis

$ mkdir /usr/local/redis/etc
$ cp redis.conf /usr/local/redis/etc
```

创建 /etc/systemd/system/redis.service 文件并添加以下内容：

```
[Unit]
Description=redis
After=network.target

[Service]
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/etc/redis.conf
ExecStop=/usr/local/redis/bin/redis-cli shutdown
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

执行以下命令：

```
$ sudo systemctl enable redis
$ sudo systemctl start redis
```

### [Rust](https://www.rust-lang.org/tools/install)

安装前执行以下命令。

```
# for toolchain
$ export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
# for rustup
$ export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup

>set RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
>set RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
```

开始安装……

```
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

>curl -O https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-gnu/rustup-init.exe
```

如果速度比较慢可以通过国内镜像加速。

```
$ curl http://mirrors.rustcc.cn/rustup/archive/1.21.1/x86_64-unknown-linux-gnu/rustup-init -o rustup-init

>curl -O http://mirrors.rustcc.cn/rustup/archive/1.21.1/x86_64-pc-windows-gnu/rustup-init.exe
```

安装前配置一些选项。

```
1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
>2

Default host triple?
# Windows: x86_64-pc-windows-gnu
x86_64-unknown-linux-gnu

Default toolchain? (stable/beta/nightly/none)
stable

Profile (which tools and data to install)? (minimal/default/complete)
default

Modify PATH variable? (y/n)
y
```

运行一下。

```
$ source ~/.cargo/env
```

如果需要卸载Rust环境，可以这么做：

```
$ rustup self uninstall
```

为设置镜像源，创建 ~/.cargo/config 文件并添加以下内容：

```
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = "ustc"

[source.ustc]
registry = "https://mirrors.ustc.edu.cn/crates.io-index"
```

### [SQLite](https://www.sqlite.org/download.html)

提取相应的包。

```
$ tar -xzvf sqlite-autoconf-3310100.tar.gz
$ cd sqlite-autoconf-3310100
$ ./configure
$ make
$ sudo make install
```

### [SWIG](http://www.swig.org/download.html)

提取相应的包。

```
$ tar -xzvf swig-4.0.2.tar.gz
$ cd swig-4.0.2

$ cp /path/to/pcre-8.44.tar.gz .
$ sh Tools/pcre-build.sh

$ ./configure --prefix=/usr/local/swig
$ make
$ sudo make install
```

### [Valgrind](https://www.valgrind.org/downloads/current.html)

提取相应的包。

```
$ tar -xjvf valgrind-3.15.0.tar.bz2
$ cd valgrind-3.15.0
$ ./configure --prefix=/usr/local/valgrind
$ make
$ sudo make install
```

## 部分依赖apt/yum方式安装软件

有时候不得不依赖包管理器。

### [Lua](https://www.lua.org/manual/5.3/readme.html)

安装依赖。

```
$ sudo apt install libreadline-dev
```

略。

```
$ curl -O https://www.lua.org/ftp/lua-5.3.5.tar.gz
$ tar -xzvf lua-5.3.5.tar.gz
$ cd lua-5.3.5
$ make linux
$ sudo make install
```

通过 luac 将 lua 文件编译为字节码。

```
$ echo -e '#!/usr/local/bin/lua\nprint("Hello World!")' > main.lua
$ luac -o main.luo main.lua
$ lua main.luo
```

### [pybind11](https://pybind11.readthedocs.io/en/master/basics.html)

安装Python的开发包。

```
$ sudo apt install python3-dev
```

安装pytest。

```
$ sudo apt install python3-pip
$ pip3 install pytest
```

通过 git 获取源代码。

```
$ sudo apt install git
$ git clone https://github.com/pybind/pybind11.git
$ cd pybind11
```

编译并安装pybind11。

```
$ cmake -S . -B build
$ cd build
$ make
$ sudo make install
```

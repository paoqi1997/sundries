# install

一些软件的安装指引。

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

对指定 URL 进行压测操作。

```
$ ./support/ab -c 10 -n 100 http://127.0.0.1:8080/
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

设置 GOPATH 等。

```
$ go env -w GOPATH=$HOME/ws
$ go env -w GO111MODULE=on
```

设置[模块代理](https://goproxy.cn)。

```
$ go env -w GOPROXY=https://goproxy.cn,direct
```

### [GoogleTest](https://github.com/google/googletest)

通过 git 获取源代码。

```
$ git clone https://github.com/google/googletest.git
$ cd googletest
```

编译并安装googletest。

```
$ cmake -S . -B build
$ cd build
$ make -j2
$ sudo make install
```

### [KCP](https://github.com/skywind3000/kcp)

通过 git 获取源代码。

```
$ git clone https://github.com/skywind3000/kcp.git
$ cd kcp
```

编译并安装kcp。

```
$ cmake -S . -B build
$ cd build
$ make -j2
$ sudo make install
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

以 root 用户执行以下命令。

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

以 root 用户执行以下命令。

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

### [xmake](https://xmake.io/#/zh-cn/guide/installation)

以非 root 用户执行以下命令。

```
$ bash <(curl -fsSL https://xmake.io/shget.text)
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

### [pybind11](https://pybind11.readthedocs.io/en/stable/basics.html)

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

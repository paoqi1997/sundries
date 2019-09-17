# 简述

面向Linux的基本教程。

# 说明

以下命令均在elementary OS 5.0下调试通过。

# 常规操作

照做，便是。

## 更换软件镜像

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

## 非apt/yum方式安装软件

能不用包管理器就不用包管理器。

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
$ sudo tar -C /usr/local -xzvf go1.10.7.linux-amd64.tar.gz
```

在$HOME/.profile文件中添加以下命令。

```
export PATH=$PATH:/usr/local/go/bin
```

运行一下。

```
$ source $HOME/.profile
```

### [MariaDB](https://mariadb.com/kb/en/library/installing-mariadb-binary-tarballs/)

在root模式下执行以下命令。

```
$ groupadd mysql

$ useradd -g mysql mysql

$ tar -C /usr/local -xzvf mariadb-10.3.13-linux-x86_64.tar.gz

$ mv /usr/local/mariadb-10.3.13-linux-x86_64 /usr/local/mysql

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

### [OpenJDK](http://jdk.java.net/archive/)

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

### [Rust](https://www.rust-lang.org/tools/install)

安装前运行以下命令。

```
# for toolchain
$ export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
# for rustup
$ export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
```

开始安装……

```
$ curl https://sh.rustup.rs -sSf | sh
```

安装前配置一些选项。

```
1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
>2

Default host triple?
x86_64-unknown-linux-gnu

Default toolchain? (stable/beta/nightly/none)
stable

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

## 部分依赖apt/yum方式安装软件

有些依赖用包管理器安装更方便一点。

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

通过git获取源代码。

```
$ sudo apt install git
$ git clone https://github.com/pybind/pybind11.git
$ cd pybind11
```

略。

```
$ mkdir build
$ cd build
$ cmake ..
$ make
$ sudo make install
```

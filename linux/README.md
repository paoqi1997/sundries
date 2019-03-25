# 简述

面向Linux的基本教程。

# 说明

以下命令均在elementary OS 5.0下调试通过。

# 常用命令

待续……

# 非apt/yum方式安装软件

有时候我们需要这么做。

## [Golang](https://golang.google.cn/doc/install)

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

## [MariaDB](https://mariadb.com/kb/en/library/installing-mariadb-binary-tarballs/)

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

拷贝脚本。

```
$ cp support-files/mysql.server /etc/init.d/mysql
```

在/etc/rc.local文件中添加以下命令。

```
service mysql start
```

设置密码。

```
$ mysqladmin -uroot password 123456
```

允许远程连接。

```sql
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
```

## [OpenJDK](http://jdk.java.net/11/)

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

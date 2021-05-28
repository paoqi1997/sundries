# The manual of RabbitMQ

面向RabbitMQ的基本教程。

## 说明

以下操作均在 elementary OS 5.1 下调试通过。

## [安装](https://rabbitmq.com/download.html)

安装依赖。

```
$ sudo apt update
$ sudo apt install \
    curl \
    gnupg \
    debian-keyring \
    debian-archive-keyring

# primary RabbitMQ signing key
$ curl -fsSL https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc | sudo apt-key add -

# Launchpad PPA signing key for apt
$ sudo apt-key adv --keyserver "keyserver.ubuntu.com" --recv-keys "F77F1EDA57EBB1CC"

$ sudo apt install apt-transport-https
```

创建 /etc/apt/sources.list.d/erlang.list 文件并添加以下内容：

```
deb https://launchpad.proxy.ustclug.org/rabbitmq/rabbitmq-erlang/ubuntu bionic main
deb-src https://launchpad.proxy.ustclug.org/rabbitmq/rabbitmq-erlang/ubuntu bionic main
```

安装Erlang。

```
$ sudo apt update
$ sudo apt install erlang-base \
    erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
    erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
    erlang-runtime-tools erlang-snmp erlang-ssl \
    erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl
```

获取 deb 包并安装之。

```
$ sudo apt install socat

$ wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.16/rabbitmq-server_3.8.16-1_all.deb
$ sudo dpkg -i rabbitmq-server_3.8.16-1_all.deb
```

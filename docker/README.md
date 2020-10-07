# The manual of Docker

面向Docker的基本教程。

## 说明

以下操作均在 Ubuntu 18.04 bionic 下调试通过。

## [安装](https://docs.docker.com/engine/install/ubuntu/)

你可通过以下途径安装Docker。

### 1. Install using the repository

相关命令如下所示：

```
$ sudo apt update
# Install packages to allow apt to use a repository over HTTPS
$ sudo apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# 添加 GPG 密钥
$ curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -

# 验证密钥
$ sudo apt-key fingerprint 0EBFCD88

# Set up the stable repository
$ sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io
```

### 2. Install from a package

从[此处](https://mirrors.aliyun.com/docker-ce/linux/ubuntu/dists/bionic/pool/stable/amd64/)获取对应的deb包。

|包名|deb名|
|--|--|
|docker-ce|docker-ce_19.03.11\~3-0\~ubuntu-bionic_amd64.deb|
|docker-ce-cli|docker-ce-cli_19.03.11\~3-0\~ubuntu-bionic_amd64.deb|
|containerd.io|containerd.io_1.2.13-2_amd64.deb|

```
$ sudo dpkg -i /path/to/package.deb
```

### 3. Install using the convenience script

相关命令如下所示：

```
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh --mirror Aliyun

$ sudo groupadd docker
# your-user是你的用户名
$ sudo usermod -aG docker your-user
```

## 配置

创建 [daemon.json](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file) 文件。

```
$ sudo touch /etc/docker/daemon.json
```

your-id是[阿里云容器镜像服务](https://cr.console.aliyun.com)为你生成的ID。

```json
{
    "registry-mirrors": [
        "https://your-id.mirror.aliyuncs.com"
    ]
}
```

## [Registry API](https://docs.docker.com/registry/spec/api/)

如果你想获取镜像列表，但又不想访问Docker Hub，那就要通过 Registry API 来实现。

在访问 Docker Registry HTTP API V2 之前，你需要获取[token](https://docs.docker.com/registry/spec/auth/token/)。

同级目录下的 listtags.py 用以获取镜像列表，希望它能帮到你。

```
# 顺利的话，相关结果会写入指定文件
$ python3 listtags.py nginx
```

## Use Docker

通过 Docker 搭建 [MySQL](https://github.com/docker-library/docs/tree/master/mysql) 服务。

```
$ docker pull mysql:8.0.19

$ docker image ls
$ docker images

$ docker run \
    -p 127.0.0.1:3306:3306 -d --rm --name mysql8 \
    -e MYSQL_ROOT_PASSWORD=123456 \
    mysql:8.0.19

$ docker container ls
$ docker ps -a

$ docker exec -it mysql8 bash
$ mysql -uroot -p123456

$ docker stop mysql8
```
# The manual of Docker

面向 Docker 的基本教程。

## 说明

以下操作均在 Ubuntu 18.04 bionic 下调试通过。

## Manage Docker

### [安装](https://docs.docker.com/engine/install/ubuntu/)

你可通过以下途径安装 Docker。

#### 1. Install using the repository

相关命令（2021-10-05 的安装方式）如下所示：

```
$ sudo apt update
$ sudo apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker’s official GPG key
$ curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 列出指定软件的版本列表
$ apt-cache madison docker-ce

$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io
```

相关命令（更早的安装方式）如下所示：

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

#### 2. Install from a package

从[此处](https://mirrors.aliyun.com/docker-ce/linux/ubuntu/dists/bionic/pool/stable/amd64/)获取对应的 deb 包。

|包名|deb名|何时安装|
|--|--:|:--:|
|docker-ce|docker-ce_20.10.9\~3-0~ubuntu-bionic_amd64.deb|2021-10-05|
|docker-ce-cli|docker-ce-cli_20.10.9\~3-0~ubuntu-bionic_amd64.deb|2021-10-05|
|containerd.io|containerd.io_1.4.11-1_amd64.deb|2021-10-05|
|docker-ce|docker-ce_19.03.11\~3-0~ubuntu-bionic_amd64.deb|更早|
|docker-ce-cli|docker-ce-cli_19.03.11\~3-0~ubuntu-bionic_amd64.deb|更早|
|containerd.io|containerd.io_1.2.13-2_amd64.deb|更早|

```
$ sudo dpkg -i /path/to/package.deb
```

#### 3. Install using the convenience script

相关命令如下所示：

```
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh --mirror Aliyun

$ sudo groupadd docker
# your-user是你的用户名
$ sudo usermod -aG docker your-user
```

### 配置

创建 [daemon.json](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file) 文件。

```
$ sudo touch /etc/docker/daemon.json
```

以下是文件要包含的内容，其中 your-id 是[阿里云容器镜像服务](https://cr.console.aliyun.com)为你生成的 ID。

```json
{
    "registry-mirrors": [
        "https://your-id.mirror.aliyuncs.com"
    ]
}
```

### 卸载

执行以下命令即可。

```
# 通过 apt 卸载
$ sudo apt purge docker-ce docker-ce-cli containerd.io
# 通过 dpkg 卸载
$ sudo dpkg -r docker-ce docker-ce-cli containerd.io

# 删除镜像、容器、卷等
$ sudo rm -rf /var/lib/docker
$ sudo rm -rf /var/lib/containerd
```

## Use Docker

### [基本命令](https://docs.docker.com/engine/reference/commandline/docker/)

以下是一些基本的命令：

```
# Display system-wide information
$ docker info

# 列出网络
$ docker network ls

# 查看镜像列表
$ docker image ls
$ docker images

# 查看容器列表
$ docker container ls
$ docker ps -a

# 附着到容器上
$ docker attach your-container

# 查看容器内运行的进程
$ docker top your-container

# 移除指定镜像
$ docker rmi -f your-image

# 停止所有正在运行的容器
$ docker stop $(docker ps -aq)
# 删除所有容器
$ docker rm $(docker ps -aq)

# Fetch the logs of a container
$ docker logs your-container

# Return low-level information on Docker objects
$ docker inspect your-container

# 在 Docker Hub 上搜索镜像
$ docker search image-name

# 查看镜像历史
$ docker history your-image --no-trunc

# 将容器中的文件拷贝到本地
$ docker cp container-id:/path/to/file .
# 将本地文件拷贝到容器中
$ docker cp file container-id:/path/to
```

#### MySQL

搭建 [MySQL](https://github.com/docker-library/docs/tree/master/mysql) 服务。

```
$ docker pull mysql:8.0.19

$ docker run \
    -p 127.0.0.1:3306:3306 -d --rm --name mysql8 \
    -e MYSQL_ROOT_PASSWORD=123456 \
    mysql:8.0.19

$ docker exec -it mysql8 bash
$ mysql -uroot -p123456

$ docker stop mysql8
```

#### Redis

准备 script.lua 脚本。

```lua
local queueKey = KEYS[1]
local lenLimit = ARGV[1]
local data = ARGV[2]

local ret = 0

-- https://redis.io/commands/lpush/
local len = redis.call('LPUSH', queueKey, data)
if len > tonumber(lenLimit) then
    redis.call('LTRIM', queueKey, 0, lenLimit - 1)
    ret = 1
end

len = redis.call('LLEN', queueKey)

return { ret, len }
```

搭建 [Redis](https://github.com/docker-library/docs/tree/master/redis) 服务。

```
$ docker pull redis:5.0.7

$ docker run \
    -p 127.0.0.1:6379:6379 -d --rm --name redis5 \
    -v $PWD/script.lua:/opt/script.lua \
    redis:5.0.7

$ docker exec -it redis5 bash

# https://redis.com/blog/5-6-7-methods-for-tracing-and-debugging-redis-lua-scripts/
$ redis-cli --eval /opt/script.lua q , 10 cqc
$ redis-cli lrange q 0 9

$ docker stop redis5
```

#### nginx

搭建 [nginx](https://github.com/docker-library/docs/tree/master/nginx) 服务并部署 [LearnOpenGL](https://github.com/LearnOpenGL-CN/LearnOpenGL-CN) 在线教程。

```
$ git clone https://github.com/LearnOpenGL-CN/LearnOpenGL-CN
$ cd LearnOpenGL-CN

$ python3 setup.py install
$ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple mkdocs
$ mkdocs build

$ docker pull nginx:1.20.1

$ docker run \
    -p 12358:80 -d --rm --name ngx-lo \
    -v $PWD/site:/usr/share/nginx/html:ro \
    nginx:1.20.1

$ curl 127.0.0.1:12358
```

### [Dockerfile](https://docs.docker.com/engine/reference/builder/)

执行以下命令即可。

```
# 构建镜像
$ docker build -t paoqi/centos:origin .

$ docker run \
    -d -it --rm --name centos7 \
    paoqi/centos:origin

$ docker exec -it centos7 bash

# 查看 CentOS 版本
$ cat /etc/centos-release
```

### [Docker Compose](https://docs.docker.com/compose/)

安装 docker-compose。

```
# https://github.com/docker/compose
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

# https://hub.docker.com/r/docker/compose
$ docker pull docker/compose
```

搭建 [PhotoPrism](https://photoprism.app) 服务。

```
# https://docs.photoprism.app/getting-started/docker-compose/
$ wget https://dl.photoprism.app/docker/docker-compose.yml

# https://docs.docker.com/compose/reference/up/
$ docker-compose up -d
```

## [Registry API](https://docs.docker.com/registry/spec/api/)

如果你想获取镜像列表，但又不想访问 [Docker Hub](https://registry.hub.docker.com) 站点的话，那就要通过 Registry API 来实现。

在访问 Docker Registry HTTP API V2 之前，你需要获取 [token](https://docs.docker.com/registry/spec/auth/token/)。

同级目录下的 listtags.py 用以获取镜像列表，希望它能帮到你。

```
# 顺利的话，相关结果会写入 nginx.tags 文件
$ python3 listtags.py nginx
```

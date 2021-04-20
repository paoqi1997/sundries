# The manual of Redis

面向Redis的基本教程。

## 说明

以下操作均在 Redis 5.0.7 下调试通过。

## [安装](https://redis.io/download)

提取相应的包。

```
$ tar -xzvf redis-5.0.7.tar.gz
$ cd redis-5.0.7
$ make
$ sudo make install PREFIX=/usr/local/redis

$ mkdir /usr/local/redis/etc
$ cp redis.conf /usr/local/redis/etc
```

创建 /lib/systemd/system/redis.service 文件并添加以下内容：

```
[Unit]
Description=redis
After=network.target

[Service]
# 如果 redis.conf 将 daemonize 设置为 yes 的话，这里需要设置 Type=forking。
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

## Use Redis

启动 redis 客户端。

```
$ redis-cli
```

执行以下命令。

```
127.0.0.1:6379> SET name paoqi
127.0.0.1:6379> GET name
```

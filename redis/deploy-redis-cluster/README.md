# 部署 Redis 集群

## 部署

为各个 Redis 实例创建 data 文件夹。

```
$ sudo mkdir -p /opt/docker/redis-cluster/{redis-m1,redis-m2,redis-m3,redis-s1,redis-s2,redis-s3}/data
```

为各个 Redis 实例准备配置文件。

```
$ echo \
    /opt/docker/redis-cluster/redis-m1 \
    /opt/docker/redis-cluster/redis-m2 \
    /opt/docker/redis-cluster/redis-m3 \
    /opt/docker/redis-cluster/redis-s1 \
    /opt/docker/redis-cluster/redis-s2 \
    /opt/docker/redis-cluster/redis-s3 | xargs -n 1 sudo cp -v redis.conf
```

创建并启动容器。

```
$ docker compose -f docker-compose.yml up -d
```

通过 Redis 容器内部的 redis-cli 创建 Redis 集群。

```
$ docker exec -it redis-m1 bash

# redis-cli --cluster create \
    172.18.9.162:6379 172.18.9.162:6479 172.18.9.162:6579 \
    172.18.9.162:6679 172.18.9.162:6779 172.18.9.162:6879 \
    --cluster-replicas 1 -a 123456

# redis-cli -c -h 172.18.9.162 -p 6379
172.18.9.162:6379> AUTH 123456
OK
172.18.9.162:6379> CLUSTER INFO
...
172.18.9.162:6379> CLUSTER NODES
...
```

单独安装 redis-cli。

```
$ sudo apt install -y redis-tools
```

在宿主机通过 redis-cli 访问 Redis 集群。

```
$ redis-cli -c -h 172.18.9.162 -p 6379 -a 123456
172.18.9.162:6379> CLUSTER SLOTS
...
172.18.9.162:6379> CLUSTER SHARDS
...
```

停止并删除容器。

```
$ docker compose -f docker-compose.yml down
```

## TPs

+ [Redis7.2.4分片集群搭建](https://blog.csdn.net/miserable_world/article/details/136674051)

+ [docker-compose搭建redis集群](https://www.yoyoask.com/?p=6051)

+ [Redis 分片集群搭建并使用 RedisTemplate 实现读写分离](https://www.cnblogs.com/studyjobs/p/17924704.html)

### Docker

+ [redis - Official Image | Docker Hub](https://hub.docker.com/_/redis)

### Redis Docs

+ [Commands](https://redis.io/docs/latest/commands/)

### Learn Redis

+ [4.1 Exercise - Creating a Redis Cluster](https://redis.io/learn/operate/redis-at-scale/scalability/exercise-1)

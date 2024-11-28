# 部署 MongoDB 集群

## 部署

为各个 MongoDB 实例创建 db 和 configdb 文件夹。

```
$ sudo mkdir -p \
    /opt/docker/mongodb-cluster/{mongos-1,mongos-2}/{db,configdb} \
    /opt/docker/mongodb-cluster/{config-server-1,config-server-2,config-server-3}/{db,configdb} \
    /opt/docker/mongodb-cluster/{shard-1a,shard-1b,shard-1c}/{db,configdb} \
    /opt/docker/mongodb-cluster/{shard-2a,shard-2b,shard-2c}/{db,configdb}
```

为 mongodb-cluster 目录下的各个文件夹增加写权限。

```
$ sudo chmod -R 777 /opt/docker/mongodb-cluster/*
```

创建并启动容器。

```
$ docker compose -f docker-compose.yml up -d
```

停止并删除容器。

```
$ docker compose -f docker-compose.yml down
```

### 为配置服务器创建副本集

进入 config-server-1 容器。

```
$ docker exec -it config-server-1 mongosh
```

调用 rs.initiate。

```js
test> rs.initiate(
  {
    _id: "rs-config",
    configsvr: true,
    members: [
      { _id : 0, host : "config_server1:27017" },
      { _id : 1, host : "config_server2:27017" },
      { _id : 2, host : "config_server3:27017" }
    ]
  }
)
```

### 为分片创建副本集

进入 shard-1a 容器。

```
$ docker exec -it shard-1a mongosh
```

调用 rs.initiate。

```js
test> rs.initiate(
  {
    _id : "rs-shard1",
    members: [
      { _id : 0, host : "shard1a:27017" },
      { _id : 1, host : "shard1b:27017" },
      { _id : 2, host : "shard1c:27017" }
    ]
  }
)
```

进入 shard-2a 容器。

```
$ docker exec -it shard-2a mongosh
```

调用 rs.initiate。

```js
test> rs.initiate(
  {
    _id : "rs-shard2",
    members: [
      { _id : 0, host : "shard2a:27017" },
      { _id : 1, host : "shard2b:27017" },
      { _id : 2, host : "shard2c:27017" }
    ]
  }
)
```

### 添加分片

进入 mongos-1 容器。

```
$ docker exec -it mongos-1 mongosh
```

调用 sh.addShard 等。

```js
test> sh.addShard("rs-shard1/shard1a:27017,shard1b:27017,shard1c:27017")
test> sh.addShard("rs-shard2/shard2a:27017,shard2b:27017,shard2c:27017")

test> sh.status()

test> sh.getBalancerState()
test> sh.isBalancerRunning()

// 创建 pq 数据库
test> sh.enableSharding("pq")
// 对 players 集合进行分片
test> sh.shardCollection("pq.players", { "_id": "hashed" })

test> use pq

pq> for (let i = 1; i <= 100; i += 1) {
  const playerId = 10000000 + i;
  db.players.insertOne({
    id: playerId,
    name: `test_${playerId}`
  });
}

// 打印分片集合的数据分布统计
pq> db.players.getShardDistribution()
```

## TPs

+ [使用docker-compose部署MongoDB shard-cluster](https://blog.csdn.net/u014448505/article/details/133480823)

+ [docker compose部署mongodb 分片集群的操作方法](https://www.jb51.net/server/3288693gf.htm)

+ [docker-compose搭建mongodb分片集群(单机版)](https://www.cnblogs.com/xiaofengxzzf/p/12100730.html)

+ [MongoDB 7.0集群部署](https://www.cnblogs.com/cn-jasonho/p/18024974)

+ [【超详细】手把手教你搭建MongoDB集群搭建](https://www.jianshu.com/p/0df3648665ec)

### Docker

+ [mongo - Official Image | Docker Hub](https://hub.docker.com/_/mongo)

+ [mongodb/mongodb-community-server - Docker Image | Docker Hub](https://hub.docker.com/r/mongodb/mongodb-community-server)

+ [Compose file reference](https://docs.docker.com/reference/compose-file/)

### MongoDB Manual

+ [部署自管理分片集群](https://www.mongodb.com/zh-cn/docs/manual/tutorial/deploy-shard-cluster/)

+ [原生分片集群方法](https://www.mongodb.com/zh-cn/docs/manual/reference/method/js-sharding/)

# Redis开发与运维·阅读笔记

《Redis开发与运维》的阅读笔记。

## 第1章 初识Redis

本章主要讲述了Redis的特性和一些使用场景，告诉我们怎么用好Redis，
除此之外还包括Redis的安装、配置、启动、关闭等操作，以及Redis的版本迭代等内容。

## 第2章 API的理解和使用

### 2.1 预备

在正式学习5种数据结构之前，最好先了解一下Redis的一些全局命令、数据结构和内部编码及单线程命令处理机制。

#### 2.1.1 全局命令

相关命令如下所示：

```
127.0.0.1:6379> SET c hiredis
127.0.0.1:6379> SET java jedis
127.0.0.1:6379> SET php phpredis

# 获取所有键
127.0.0.1:6379> KEYS *

# 插入一个类型为列表的键值对（值由多个元素组成）
127.0.0.1:6379> RPUSH mylist 0 1 2 3 4

# 获取键总数
127.0.0.1:6379> DBSIZE

# 确认键是否存在
127.0.0.1:6379> EXISTS c
127.0.0.1:6379> EXISTS cpp

# 删除键
127.0.0.1:6379> DEL c

# 设置键的过期时间
127.0.0.1:6379> EXPIRE java 5
# 查看键的剩余过期时间
127.0.0.1:6379> TTL java

# 查看键的数据结构类型
127.0.0.1:6379> TYPE php
```

#### 2.1.2 数据结构和内部编码

TYPE 命令实际返回的就是当前键的数据结构类型，它们分别是：
string（字符串）、hash（哈希）、list（列表）、set（集合）及zset（有序集合）。

实际上每种数据结构都有自己底层的内部编码实现，而且是多种实现，
Redis 会在合适的场景选择合适的内部编码。

每种数据结构都有两种以上的内部编码实现，例如 list 数据结构，
它包含了 linkedlist 和 ziplist 两种内部编码。
同时某些内部编码，例如 ziplist，可以作为多种外部数据结构的内部实现。

可以通过 OBJECT ENCODING 命令查询内部编码：

```
127.0.0.1:6379> OBJECT ENCODING php
127.0.0.1:6379> OBJECT ENCODING mylist
```

Redis 这样设计有两个好处：

1. 可以改进内部编码，而对外的数据结构和命令没有影响，这样一旦开发出更优秀的内部编码，无需改动外部数据结构和命令。
   例如 Redis 3.2 提供了 quicklist，结合了 ziplist 和 linkedlist 两者的优势，
   为列表类型提供了一种更为优秀的内部编码实现，但外部用户基本感知不到。

2. 多种内部编码实现可以在不同场景下发挥各自的优势，例如 ziplist 比较节省内存，
   但在列表元素比较多的情况下，性能会有所下降，这时 Redis 会根据配置选项将列表类型的内部实现转换为 linkedlist。

#### 2.1.3 单线程架构

Redis 是单线程处理命令的，所以一条命令从客户端到达服务端不会立刻被执行，所有命令都会进入一个队列中，然后逐个被执行。

通常来讲，单线程的处理能力要比多线程差，那为什么 Redis 使用单线程模型会达到每秒万级别的处理能力呢？可以将其归结为三点：

1. 纯内存访问，Redis 将所有数据放在内存中，内存的响应时长大约为100ns，这是 Redis 达到每秒万级别访问的重要基础。

2. 非阻塞I/O，Redis 使用 epoll 作为I/O多路复用技术的实现，
   再加上 Redis 自身的事件处理模型将 epoll 中的连接、读写、关闭都转换为事件，不在网络I/O上浪费过多的时间。

3. 单线程避免了线程切换和竞态产生的消耗。

同时单线程也带来了几个好处：

1. 单线程可以简化数据结构和算法的实现，实现并发数据结构不但困难而且开发测试比较麻烦。

2. 单线程避免了线程切换和竞态产生的消耗，对于服务端开发来说，锁和线程切换通常是性能杀手。

但是单线程会有一个问题：对于每个命令的执行时间是有要求的。
如果某个命令执行过久，会造成其他命令的阻塞，
这对 Redis 这种高性能的服务来说是致命的，所以 Redis 是面向快速执行场景的数据库。

### 2.2 字符串

#### 2.2.1 命令

相关命令如下所示：

```
# 3s后过期
127.0.0.1:6379> SETEX epoll 3 1

# 只有键不存在才可以设置成功，用于添加
127.0.0.1:6379> SETNX iocp 0

127.0.0.1:6379> GET iocp
```

以 setnx 命令为例，由于 Redis 的单线程命令处理机制，如果有多个客户端同时执行`SETNX key value`，
只有一个客户端能设置成功，setnx 可以作为分布式锁的一种实现方案，
Redis 官方给出了[使用 setnx 实现分布式锁](https://redis.io/topics/distlock)的方法。

```
127.0.0.1:6379> MSET a 1 b 2 c 3 d 4
127.0.0.1:6379> MGET a b c d
```

学会批量操作，有助于提高业务处理效率，但要注意的是每次批量操作所发送的命令数并不是无节制的，
如果数量过多可能会造成 Redis 阻塞或者网络拥塞。

```
# 自增/自减1
127.0.0.1:6379> INCR counter
127.0.0.1:6379> DECR counter

# 自增/自减2
127.0.0.1:6379> INCRBY counter 2
127.0.0.1:6379> DECRBY counter 2
```

很多存储系统和编程语言内部使用 CAS 机制实现计数功能，会有一定的 CPU 开销，
但在 Redis 中完全不存在这个问题，因为 Redis 是单线程架构，任何命令到了 Redis 服务端都要按序执行。

```
127.0.0.1:6379> SET s Hello

127.0.0.1:6379> APPEND s ' World!'

127.0.0.1:6379> STRLEN s

# 设置并返回原值
127.0.0.1:6379> GETSET s 'Hello MySQL!'
127.0.0.1:6379> GETSET s 'Hello Redis!'

# 设置指定位置的字符
127.0.0.1:6379> SETRANGE s 6 J

# 获取'Redis'子串
127.0.0.1:6379> GETRANGE s 6 10
```

#### 2.2.2 内部编码

如下所示。

```
127.0.0.1:6379> SET s 123456789
127.0.0.1:6379> OBJECT ENCODING s # "int"

# <= 44bytes
127.0.0.1:6379> SET s c
127.0.0.1:6379> OBJECT ENCODING s # "embstr"

# >= 45bytes
127.0.0.1:6379> SET s '123456789012345678901234567890123456789012345'
127.0.0.1:6379> OBJECT ENCODING s # "raw"
```

#### 2.2.3 典型使用场景

主要有以下几个使用场景：

1. 缓存功能
2. 计数（比如计算视频播放数）
3. 共享Session
4. 限速（比如限制用户每分钟获取验证码的频率）

### 2.3 哈希

在 Redis 中，哈希类型是指键对应的值本身又是键值对结构。

#### 2.3.1 命令

相关命令如下所示：

```
127.0.0.1:6379> HSET clients c hiredis
127.0.0.1:6379> HSET clients java jedis

127.0.0.1:6379> HGET clients c

127.0.0.1:6379> HDEL clients c

# 计算 field 个数
127.0.0.1:6379> HLEN clients

127.0.0.1:6379> HMSET clients php phpredis go go-redis
127.0.0.1:6379> HMGET clients php go

# 确认 field 是否存在
127.0.0.1:6379> HEXISTS clients php

# 获取所有field
127.0.0.1:6379> HKEYS clients

# 获取所有value
127.0.0.1:6379> HVALS clients

# 获取所有field-value
127.0.0.1:6379> HGETALL clients

# 自增
127.0.0.1:6379> HINCRBY clients counter 2
127.0.0.1:6379> HINCRBYFLOAT clients counter 3.1

# 计算 value 长度
127.0.0.1:6379> HSTRLEN clients php
```

#### 2.3.2 内部编码

哈希类型的内部编码有两种：

1. ziplist（压缩列表）：
   当元素个数 <= hash-max-ziplist-entries（默认为512）同时所有值 <= hash-max-ziplist-value（默认为64）时，
   Redis 会使用 ziplist 作为哈希的内部实现，ziplist 使用更加紧凑的结构实现多个元素的连续存储，
   所以在节省内存方面比 hashtable 更加优秀。

2. hashtable（哈希表）：
   当哈希类型无法满足 ziplist 的条件时，Redis 会使用 hashtable 作为哈希的内部实现，
   因为此时 ziplist 的读写效率会下降，而 hashtable 的读写时间复杂度为O(1)。

```
# <= 64bytes
127.0.0.1:6379> HSET clients s '1234567890123456789012345678901234567890123456789012345678901234'
127.0.0.1:6379> OBJECT ENCODING clients # "ziplist"

# >= 65bytes
127.0.0.1:6379> HSET clients s '12345678901234567890123456789012345678901234567890123456789012345'
127.0.0.1:6379> OBJECT ENCODING clients # "hashtable"
```

#### 2.3.3 使用场景

可用于缓存用户信息等。

### 2.4 列表

列表（list）类型用来存储多个有序的字符串，一个列表最多可以存储 2^32 - 1 个元素。

列表类型有两个特点：第一，列表中的元素是有序的，这里的序是指插入顺序；第二，列表中的元素是可以重复的。

#### 2.4.1 命令

相关命令如下所示：

```
127.0.0.1:6379> RPUSH mylist c b a
127.0.0.1:6379> LPUSH mylist d e f

# 在元素a前面插入1
127.0.0.1:6379> LINSERT mylist BEFORE a 1

# 获取[0, 3]的元素
127.0.0.1:6379> LRANGE mylist 0 3
# 获取[-3, -1]的元素
127.0.0.1:6379> LRANGE mylist -3 -1

# 获取指定索引的元素
127.0.0.1:6379> LINDEX mylist 5
127.0.0.1:6379> LINDEX mylist -2

127.0.0.1:6379> LLEN mylist

127.0.0.1:6379> LPOP mylist
127.0.0.1:6379> RPOP mylist

# 删除所有值为1的元素
127.0.0.1:6379> LREM mylist 0 1

# 只保留[1, 3]的元素
127.0.0.1:6379> LTRIM mylist 1 3

# 将第一个元素修改为p
127.0.0.1:6379> LSET mylist 0 p

# 阻塞式弹出
127.0.0.1:6379> BLPOP mylist 1
127.0.0.1:6379> BRPOP mylist 3
```

当列表为空的时候，若 timeout = 3，那么客户端要等到3s后返回，如果 timeout = 0，
那么客户端会一直阻塞等下去。如果期间插入了元素，客户端将立即返回。

当列表不为空的时候，客户端会立即返回。

在使用 BRPOP 的时候，如果是多个键，那么 BRPOP 会从左到右遍历键，
一旦有一个键能弹出元素，客户端将立即返回。

如果多个客户端对同一个键执行 BRPOP 命令，那么最先执行 BRPOP 命令的客户端可以获取到弹出的值。

#### 2.4.2 内部编码

列表类型的内部编码有两种：

1. ziplist（压缩列表）：
   在 [Redis 3.0](https://raw.githubusercontent.com/redis/redis/3.0/redis.conf) 版本，
   当元素个数 <= list-max-ziplist-entries（默认为512）同时所有值 <= list-max-ziplist-value（默认为64）时，
   Redis 会使用 ziplist 作为列表的内部实现以减少内存的使用。
   但从 [Redis 3.2](https://raw.githubusercontent.com/redis/redis/3.2/redis.conf) 版本开始不再支持这两个配置选项。

2. linkedlist（链表）：
   当列表类型无法满足 ziplist 的条件时，Redis 会使用 linkedlist 作为列表的内部实现。

Redis 3.2 提供了 quicklist 内部编码，简单来说它是以一个 ziplist 为节点的 linkedlist，
它结合了 ziplist 和 linkedlist 两者的优势，为列表类型提供了一种更为优秀的内部编码实现。
它的设计原理可以参考 Redis 的另一个作者 Matt Stancliff 的[博客](https://matt.sh/redis-quicklist)。

#### 2.4.3 使用场景

主要有以下几个使用场景：

1. 消息队列

   Redis 的 LPUSH + BRPOP 命令组合即可实现阻塞队列，生产者客户端使用 LPUSH 命令从左侧插入元素，
   多个消费者客户端使用 BRPOP 命令阻塞式地“抢”列表尾部的元素。

2. 文章列表

   每个用户有属于自己的文章列表，现需要分页展示文章列表。
   此时可以考虑使用列表，因为列表不但是有序的，还支持按照索引范围获取元素。

### 2.5 集合

集合（set）类型用来保存多个字符串元素，但和列表类型不一样的是，
集合中不允许有重复元素，并且集合中的元素是无序的，不能通过索引下标获取元素。

一个集合最多可以存储 2^32 - 1 个元素。

Redis 除了支持集合内的增删改查，还支持多个集合间取交集、并集及差集。

#### 2.5.1 命令

集合内操作的相关命令如下所示：

```
127.0.0.1:6379> SADD myset a b c
127.0.0.1:6379> SREM myset a b

# 计算元素个数
127.0.0.1:6379> SCARD myset

# 确认元素是否在集合中
127.0.0.1:6379> SISMEMBER myset c

# 随机返回集合中指定个数的元素
127.0.0.1:6379> SRANDMEMBER myset 3

# 随机从集合弹出元素
127.0.0.1:6379> SPOP myset 1

# 获取所有元素
127.0.0.1:6379> SMEMBERS myset
```

集合间操作的相关命令如下所示：

```
127.0.0.1:6379> SADD user:1:follow music news sport vlog
127.0.0.1:6379> SADD user:2:follow food game news vlog

# 交集
127.0.0.1:6379> SINTER user:1:follow user:2:follow
# 并集
127.0.0.1:6379> SUNION user:1:follow user:2:follow
# 差集（返回所有给定 key 与第一个 key 的差集，这里的结果为属于1但不属于2的元素）
127.0.0.1:6379> SDIFF user:1:follow user:2:follow

# 保存交集的结果
127.0.0.1:6379> SINTERSTORE user:1_2:inter user:1:follow user:2:follow
# 保存并集的结果
127.0.0.1:6379> SUNIONSTORE user:1_2:union user:1:follow user:2:follow
# 保存差集的结果
127.0.0.1:6379> SDIFFSTORE user:1_2:diff user:1:follow user:2:follow
```

#### 2.5.2 内部编码

集合类型的内部编码有两种：

1. intset（整数集合）：
   当集合中的元素都是整数且元素个数 <= set-max-intset-entries（默认为512）时，
   Redis 会使用 intset 作为集合的内部实现，从而减少内存的使用。

2. hashtable（哈希表）：
   当集合类型无法满足 intset 的条件时，Redis 会使用 hashtable 作为集合的内部实现。

#### 2.5.3 使用场景

主要有以下几个使用场景：

1. SADD = Tagging（标签）
2. SPOP/SRANDMEMBER = Random item（生成随机数，比如抽奖）
3. SADD + SINTER = Social Graph（社交需求）

### 2.6 有序集合

有序集合保留了集合不能有重复成员的特性，但与集合不同的是，有序集合中的元素可以排序。

但它和列表使用索引下标作为排序依据不同的是，它给每个元素设置一个分数（score）作为排序依据。

#### 2.6.1 命令

集合内操作的相关命令如下所示：

```
127.0.0.1:6379> ZADD ranking 138 paoqi 96 jessica 113 chen 124 lucia 74 daisy
127.0.0.1:6379> ZREM ranking jessica

# 计算成员个数
127.0.0.1:6379> ZCARD ranking

# 获取指定成员的分数
127.0.0.1:6379> ZSCORE ranking paoqi
# 增加指定成员的分数
127.0.0.1:6379> ZINCRBY ranking 4 paoqi

# 按分数从低到高的顺序，获取指定成员的排名
127.0.0.1:6379> ZRANK ranking paoqi
# 按分数从高到低的顺序，获取指定成员的排名
127.0.0.1:6379> ZREVRANK ranking paoqi

# 按分数从低到高的顺序，获取第0个到第2个成员
127.0.0.1:6379> ZRANGE ranking 0 2 WITHSCORES
# 按分数从高到低的顺序，获取第0个到第2个成员
127.0.0.1:6379> ZREVRANGE ranking 0 2 WITHSCORES

# 按分数从低到高的顺序，获取90到120分的成员
127.0.0.1:6379> ZRANGEBYSCORE ranking 90 120 WITHSCORES
# 按分数从高到低的顺序，获取120到90分的成员
127.0.0.1:6379> ZREVRANGEBYSCORE ranking 120 90 WITHSCORES

# 按分数从低到高的顺序，获取所有成员
127.0.0.1:6379> ZRANGEBYSCORE ranking -inf +inf WITHSCORES

# 获取指定分数范围的成员个数
127.0.0.1:6379> ZCOUNT ranking 100 140

# 按分数从低到高的顺序，删除第0个到第2个成员
127.0.0.1:6379> ZREMRANGEBYRANK ranking 0 2
# 按分数从低到高的顺序，删除90分以下（不包括90分）的成员
127.0.0.1:6379> ZREMRANGEBYSCORE ranking -inf (90
```

集合间操作的相关命令如下所示：

```
127.0.0.1:6379> ZADD course1 128 paoqi 147 wendy 106 jimmy 112 liu
127.0.0.1:6379> ZADD course2 124 paoqi 102 wendy 143 jimmy 96 jackson

# 对 course1 和 course2 做交集，其中1的权重为1，2的权重为0.8，用 SUM 方法做汇总
127.0.0.1:6379> ZINTERSTORE course:1_inter_2 2 course1 course2 WEIGHTS 1 0.8 AGGREGATE SUM
127.0.0.1:6379> ZRANGEBYSCORE course:1_inter_2 -inf +inf WITHSCORES

# 对 course1 和 course2 做并集，其中1的权重为0.95，2的权重为1.15，用 SUM 方法做汇总
127.0.0.1:6379> ZUNIONSTORE course:1_union_2 2 course1 course2 WEIGHTS 0.95 1.15 AGGREGATE SUM
127.0.0.1:6379> ZRANGEBYSCORE course:1_union_2 -inf +inf WITHSCORES
```

#### 2.6.2 内部编码

有序集合类型的内部编码有两种：

1. ziplist（压缩列表）：
   当元素个数 <= zset-max-ziplist-entries（默认为512）同时所有值 <= zset-max-ziplist-value（默认为64）时，
   Redis 会使用 ziplist 作为有序集合的内部实现，ziplist 可以有效减少内存的使用。

2. skiplist（跳跃表）：
   当有序集合类型无法满足 ziplist 的条件时，Redis 会使用 skiplist 作为有序集合的内部实现，
   因为此时 ziplist 的读写效率会下降。

```
# <= 64bytes
127.0.0.1:6379> ZADD myzset 1 '1234567890123456789012345678901234567890123456789012345678901234'
127.0.0.1:6379> OBJECT ENCODING myzset # "ziplist"

127.0.0.1:6379> ZRANGEBYSCORE myzset -inf +inf WITHSCORES

# >= 65bytes
127.0.0.1:6379> ZADD myzset 1 '12345678901234567890123456789012345678901234567890123456789012345'
127.0.0.1:6379> OBJECT ENCODING myzset # "skiplist"
```

#### 2.6.3 使用场景

对于视频网站来说，主要有以下几个使用场景：

1. ZADD + ZINCRBY = 用户上传视频并获得播放量
2. ZREM = 下架用户视频
3. ZREVRANGE = 前N个播放量最多的视频
4. ZSCORE/ZREVRANK = 获取指定视频的播放量/播放量排名

### 2.7 键管理

#### 2.7.1 单个键管理

#### 2.7.2 遍历键

#### 2.7.3 数据库管理

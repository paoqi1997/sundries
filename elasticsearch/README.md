# The manual of Elasticsearch

面向 [Elasticsearch](https://www.elastic.co/cn/elasticsearch/) 的基本教程。

## 说明

以下操作均在 Ubuntu 20.04.4 LTS 下调试通过。

## [Install](https://www.elastic.co/guide/en/elasticsearch/reference/8.1/targz.html)

获取 tar 包。

```
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.1.3-linux-x86_64.tar.gz
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.1.3-linux-x86_64.tar.gz.sha512
$ shasum -a 512 -c elasticsearch-8.1.3-linux-x86_64.tar.gz.sha512

$ tar -xzvf elasticsearch-8.1.3-linux-x86_64.tar.gz
$ cd elasticsearch-8.1.3
```

在 ./config/elasticsearch.yml 文件中添加以下内容：

```
action.auto_create_index: .monitoring*,.watches,.triggered_watches,.watcher-history*,.ml*
```

在 ./config/jvm.options 文件中设置以下内容：

```
-Xms2g
-Xmx2g
```

启动。

```
# 启动成功后会打印 Password for the elastic user，后面设置 ESPASS 的时候会用到
$ ./bin/elasticsearch
```

检查 es 是否在运行。

```
$ export ES_PATH_CONF=$PWD/config
$ curl --cacert $ES_PATH_CONF/certs/http_ca.crt -u elastic https://localhost:9200
```

修改密码。

```
# https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-users.html
$ export ESPASS=password-of-elastic
$ curl -X POST --cacert $ES_PATH_CONF/certs/http_ca.crt \
    -u elastic:$ESPASS "https://localhost:9200/_security/user/elastic/_password?pretty" \
    -H 'Content-Type: application/json' -d '{ "password": "123456" }'

# 重置密码
$ ./bin/elasticsearch-reset-password -u elastic
```

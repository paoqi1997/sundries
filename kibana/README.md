# The manual of Kibana

面向 [Kibana](https://www.elastic.co/cn/kibana/) 的基本教程。

## 说明

以下操作均在 Ubuntu 20.04.4 LTS 下调试通过。

## [Install](https://www.elastic.co/guide/en/kibana/8.1/targz.html)

获取 tar 包。

```
$ curl -O https://artifacts.elastic.co/downloads/kibana/kibana-8.1.3-linux-x86_64.tar.gz
$ curl https://artifacts.elastic.co/downloads/kibana/kibana-8.1.3-linux-x86_64.tar.gz.sha512 | shasum -a 512 -c -

$ tar -xzvf kibana-8.1.3-linux-x86_64.tar.gz
$ cd kibana-8.1.3
```

在 ./config/kibana.yml 文件中设置以下内容：

```
# Kibana is served by a back end server. This setting specifies the port to use.
server.port: 5601

# The URLs of the Elasticsearch instances to use for all your queries.
elasticsearch.hosts: ["http://localhost:9200"]

# If your Elasticsearch is protected with basic authentication, these settings provide
# the username and password that the Kibana server uses to perform maintenance on the Kibana
# index at startup. Your Kibana users still need to authenticate with Elasticsearch, which
# is proxied through the Kibana server.
elasticsearch.username: "kibana_system"
elasticsearch.password: "pass"
```

启动。

```
$ ./bin/kibana
```

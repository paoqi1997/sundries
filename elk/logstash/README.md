# The manual of Logstash

面向 [Logstash](https://www.elastic.co/cn/logstash/) 的基本教程。

## 说明

以下操作均在 Ubuntu 20.04.4 LTS 下调试通过。

## [Install](https://www.elastic.co/guide/en/logstash/8.1/installing-logstash.html)

获取 tar 包。

```
$ curl -O https://artifacts.elastic.co/downloads/logstash/logstash-8.1.3-linux-x86_64.tar.gz
$ curl -O https://artifacts.elastic.co/downloads/logstash/logstash-8.1.3-linux-x86_64.tar.gz.sha512
$ shasum -a 512 -c logstash-8.1.3-linux-x86_64.tar.gz.sha512

$ tar -xzvf logstash-8.1.3-linux-x86_64.tar.gz
$ cd logstash-8.1.3
```

启动最简单的 logstash 管道。

```
$ ./bin/logstash -e 'input { stdin { } } output { stdout {} }'

# 启动后在该会话输入内容，会看到相应的输出
```

### 集成 Filebeat

安装 [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/8.1/filebeat-installation-configuration.html)。

```
$ curl -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.1.3-linux-x86_64.tar.gz
$ tar -xzvf filebeat-8.1.3-linux-x86_64.tar.gz
$ cd filebeat-8.1.3-linux-x86_64
```

在 ./filebeat.yml 文件中设置以下内容：

```yml
filebeat.inputs:
- type: log
  paths:
    - /path/to/file/logstash-what.log
# 只发往 logstash，注释掉 output.elasticsearch
output.logstash:
  hosts: ["localhost:5044"]
```

开始监视文件。

```
$ ./filebeat -e -c filebeat.yml -d "publish"
```

配置 logstash-sample.conf 文件：

```
# Sample Logstash configuration for creating a simple
# Beats -> Logstash -> Elasticsearch pipeline.

input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => ["https://localhost:9200"]
    cacert => "/path/to/file/sslconfig/kibana/elasticsearch-ca.pem"
    index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
    # logstash_system
    user => "elastic"
    password => "123456"
  }
}
```

启动。

```
$ ./bin/logstash -f config/logstash-sample.conf --config.reload.automatic
```

准备并查看数据。

```
$ curl -X PUT -k -u elastic:123456 https://localhost:9200/filebeat-8.1.3-2022.06.13

$ touch logstash-what.log
$ echo "Hello!" >> logstash-what.log

$ curl -k -u elastic:123456 https://localhost:9200/_cat/indices
$ curl -k -u elastic:123456 https://localhost:9200/filebeat-8.1.3-2022.06.13/_search
```

相关参考链接如下所示：

+ [配置 SSL、TLS 以及 HTTPS 来确保 Elasticsearch、Kibana、Beats 和 Logstash 的安全](https://www.elastic.co/cn/blog/configuring-ssl-tls-and-https-to-secure-elasticsearch-kibana-beats-and-logstash)

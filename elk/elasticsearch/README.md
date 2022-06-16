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

```yml
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

修改 elastic 用户的密码。

```
# https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-users.html
$ export ESPASS=password-of-elastic
$ curl -X POST --cacert $ES_PATH_CONF/certs/http_ca.crt \
    -u elastic:$ESPASS "https://localhost:9200/_security/user/elastic/_password?pretty" \
    -H 'Content-Type: application/json' -d '{ "password": "123456" }'

# 重置密码
$ ./bin/elasticsearch-reset-password -u elastic
```

### 使 Kibana 能与经 HTTPS 加密的 es 通信

修改 kibana_system 用户的密码。

```
$ curl -X POST --cacert $ES_PATH_CONF/certs/http_ca.crt \
    -u elastic:123456 "https://localhost:9200/_security/user/kibana_system/_password?pretty" \
    -H 'Content-Type: application/json' -d '{ "password": "123456" }'
```

准备 CA。

```
# 默认生成 elastic-stack-ca.p12 文件，这里可以设置密码，比如 abc
$ ./bin/elasticsearch-certutil ca

# 默认生成 elastic-certificates.p12 文件
$ ./bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12
```

生成证书。

```
$ ./bin/elasticsearch-certutil http
...
Generate a CSR? [y/N]
<ENTER>
...
Use an existing CA? [y/N]y
...
CA Path: /path/to/elastic-stack-ca.p12
...
# 这里填 abc
Password for elastic-stack-ca.p12:
...
For how long should your certificate be valid? [5y] 1y
...
# 单机部署，先忽略
Generate a certificate per node? [y/N]
<ENTER>
...
Enter all the hostnames that you need, one per line.
When you are done, press <ENTER> once more to move on to the next step.
localhost
<ENTER>
...
Enter all the IP addresses that you need, one per line.
When you are done, press <ENTER> once more to move on to the next step.
127.0.0.1
<ENTER>
...
Do you wish to change any of these options? [y/N]
<ENTER>
...
# 这里填 xyz
Provide a password for the "http.p12" file:  [<ENTER> for none]
Repeat password to confirm:
...
What filename should be used for the output zip file? [/path/to/elasticsearch-ssl-http.zip]
<ENTER>
```

将相关文件拷贝到 config 目录。

```
$ unzip elasticsearch-ssl-http.zip -d sslconfig
$ cp sslconfig/elasticsearch/http.p12 config/certs/httplus.p12
$ cp sslconfig/kibana/elasticsearch-ca.pem ../kibana-8.1.3/config
```

更新 http.ssl 方面的密码。

```
# 填入之前设置的 xyz
$ ./bin/elasticsearch-keystore add xpack.security.http.ssl.keystore.secure_password
Setting xpack.security.http.ssl.keystore.secure_password already exists. Overwrite? [y/N]y
Enter value for xpack.security.http.ssl.keystore.secure_password:
```

在 ./config/elasticsearch.yml 文件中修改 keystore.path 选项：

```yml
# Enable encryption for HTTP API client connections, such as Kibana, Logstash, and Agents
xpack.security.http.ssl:
  enabled: true
  keystore.path: certs/httplus.p12
```

curl 用新证书访问 es。

```
$ curl --cacert sslconfig/kibana/elasticsearch-ca.pem -u elastic:123456 https://localhost:9200
$ curl -k -u elastic:123456 https://localhost:9200
```

相关参考链接如下所示：

+ [Secure the Elastic Stack](https://www.elastic.co/guide/en/elasticsearch/reference/8.1/secure-cluster.html)

+ [从0开始在Elastic Stack中完成TLS加密](https://www.rondochen.com/ELK9/)

+ [ElasticSearch安全-账号密码验证](https://www.cnblogs.com/luo630/p/15341532.html)

+ [A step-by-step guide to enabling security, TLS/SSL, and PKI authentication in Elasticsearch](https://alexmarquardt.com/2018/11/05/security-tls-ssl-pki-authentication-in-elasticsearch/)

### 引入 elasticsearch-head

为解决跨域问题，在 ./config/elasticsearch.yml 文件中添加以下内容：

```yml
# Enable security features
xpack.security.enabled: false

# https://www.elastic.co/guide/en/elasticsearch/reference/8.1/modules-network.html
http.cors.enabled: true
http.cors.allow-origin: "*"
```

部署 ElasticSearch Head。

```
$ git clone https://github.com/mobz/elasticsearch-head
$ cd elasticsearch-head

$ npm install
$ npm run start
```

在浏览器访问该链接：`http://127.0.0.1:9100`

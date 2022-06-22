# The manual of Prometheus

面向 [Prometheus](https://prometheus.io) 的基本教程。

## 说明

以下操作均在 Ubuntu 20.04.4 LTS 下调试通过。

## [Install](https://prometheus.io/docs/prometheus/2.36/getting_started/)

获取 tar 包。

```
$ curl -LO https://github.com/prometheus/prometheus/releases/download/v2.36.2/prometheus-2.36.2.linux-amd64.tar.gz

$ tar -xzvf prometheus-2.36.2.linux-amd64.tar.gz
$ mv prometheus-2.36.2.linux-amd64 prometheus-2.36.2
$ cd prometheus-2.36.2
```

准备集成 node_exporter。

```
$ curl -LO https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz

$ tar -xzvf node_exporter-1.3.1.linux-amd64.tar.gz
$ mv node_exporter-1.3.1.linux-amd64 node_exporter-1.3.1
$ cd node_exporter-1.3.1

$ ./node_exporter --web.listen-address 127.0.0.1:8280
$ ./node_exporter --web.listen-address 127.0.0.1:8281
$ ./node_exporter --web.listen-address 127.0.0.1:8282
```

在 ./prometheus.yml 文件中设置以下内容：

```yml
# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  - 'prometheus.rules.yml'

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]

  # 为 node_exporter 准备的
  - job_name: 'node'

    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 5s

    static_configs:
      - targets: ['localhost:8280', 'localhost:8281']
        labels:
          group: 'production'

      - targets: ['localhost:8282']
        labels:
          group: 'canary'
```

创建 prometheus.rules.yml 文件并添加以下内容：

```yml
groups:
- name: cpu-node
  rules:
  - record: job_instance_mode:node_cpu_seconds:avg_rate5m
    expr: avg by (job, instance, mode) (rate(node_cpu_seconds_total[5m]))
```

启动，然后会发现 node_exporter 提示 `remote error: tls: bad certificate`。

```
$ ./prometheus
```

### 启用 TLS

准备证书。

```
$ mkdir prometheus-tls
$ cd prometheus-tls

$ openssl req -new -newkey rsa:2048 -days 365 -nodes \
  -x509 -keyout node_exporter.key -out node_exporter.crt \
  -subj "/C=BE/ST=Guangdong/L=Guangzhou/O=PQ/CN=localhost" -addext "subjectAltName = DNS:localhost"

$ cp node_exporter.crt node_exporter.key ../node_exporter-1.3.1
```

创建 config.yml 文件并添加以下内容：

```yml
tls_server_config:
  cert_file: node_exporter.crt
  key_file: node_exporter.key
```

重新启动 node_exporter。

```
$ ./node_exporter --web.config=config.yml --web.listen-address 127.0.0.1:8280
$ ./node_exporter --web.config=config.yml --web.listen-address 127.0.0.1:8281
$ ./node_exporter --web.config=config.yml --web.listen-address 127.0.0.1:8282
```

在 ./prometheus.yml 文件中添加以下内容：

```yml
scrape_configs:
  - job_name: 'node'

    # # scheme defaults to 'http'.
    scheme: https

    tls_config:
      ca_file: node_exporter.crt
```

再次启动。

```
$ ./prometheus
```

在浏览器访问该链接：`http://127.0.0.1:9090`，然后在 Expression 框输入 `job_instance_mode:node_cpu_seconds:avg_rate5m`，点击 Execute 并查看结果。

相关参考链接如下所示：

+ [为 Prometheus Node Exporter 加上认证（腾讯云）](https://cloud.tencent.com/developer/article/1634856)

+ [为 Prometheus Node Exporter 加上认证（知乎）](https://zhuanlan.zhihu.com/p/144048025)

+ [Prometheus Server and TLS](https://inuits.eu/blog/prometheus-server-tls/)

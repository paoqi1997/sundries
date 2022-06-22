# The manual of Grafana

面向 [Grafana](https://grafana.com) 的基本教程。

## 说明

以下操作均在 Ubuntu 20.04.4 LTS 下调试通过。

## [Install](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

获取 tar 包。

```
$ wget https://dl.grafana.com/enterprise/release/grafana-enterprise-9.0.1.linux-amd64.tar.gz

$ tar -xzvf grafana-enterprise-9.0.1.linux-amd64.tar.gz
$ cd grafana-9.0.1
```

启动。

```
$ ./bin/grafana-server
```

## [Work with Prometheus](https://grafana.com/docs/grafana/latest/getting-started/get-started-grafana-prometheus/)

在浏览器访问该链接：`http://127.0.0.1:3000`，登录 Grafana，账号和密码均为 admin（可在 defaults.ini 配置文件中修改）。

点击 Data sources 或者访问 `http://127.0.0.1:3000/datasources`，添加 Prometheus 数据源。

点击 Dashboards -> Import 或者访问 `http://localhost:3000/dashboard/import`，在 **Import via grafana.com** 一框中输入1860并点击 Load。会看到 Node Exporter Full，选择数据源后点击 **Import (Overwrite)**。

返回 Dashboards，就可以看到设置好的面板。

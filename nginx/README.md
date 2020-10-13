# The manual of NGINX

面向NGINX的基本教程。

## 说明

以下操作均在 Ubuntu 18.04 bionic 下验证通过。

## [安装](https://nginx.org/en/download.html)

获取[OpenSSL](https://www.openssl.org/source/)、[PCRE](https://ftp.pcre.org/pub/pcre/)及[zlib](https://zlib.net)的包后，提取nginx的包。

```
$ tar -xzvf nginx-1.16.1.tar.gz
$ cd nginx-1.16.1

$ ./configure --with-http_ssl_module --with-http_stub_status_module \
    --with-openssl=../openssl-1.1.1d --with-pcre=../pcre-8.44 --with-zlib=../zlib-1.2.11

$ make
$ sudo make install
```

创建 /etc/systemd/system/[nginx.service](https://www.nginx.com/resources/wiki/start/topics/examples/systemd/) 文件并添加以下内容：

```
[Unit]
Description=The NGINX HTTP and reverse proxy server
After=network.target

[Service]
Type=forking
ExecStartPre=/usr/local/nginx/sbin/nginx -t
ExecStart=/usr/local/nginx/sbin/nginx
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/usr/local/nginx/sbin/nginx -s quit
Restart=on-failure
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

执行以下命令：

```
$ sudo systemctl enable nginx
$ sudo systemctl start nginx
```

## 配置

适用于不同的应用场景的 nginx.conf 如下所示。

### 负载均衡

```conf
worker_processes  2;

events {
    use  epoll;
    worker_connections  1024;
}

http {
    upstream httpds {
        server  127.0.0.1:8080;
        server  127.0.0.1:8088;
    }

    server {
        listen  80;

        location / {
            proxy_pass  http://httpds;
        }
    }
}
```

### 图片服务器

```conf
user  www-data;
worker_processes  auto;
error_log  /var/www/error.log  info;

events {
    use  epoll;
    worker_connections  1024;
}

http {
    gzip         on;
    sendfile     on;
    tcp_nopush   on;
    tcp_nodelay  on;

    keepalive_timeout  60;
    include            mime.types;
    default_type       application/octet-stream;

    log_format  main  '[$time_local] ip: $remote_addr req: "$request" '
                      'status: $status size: $body_bytes_sent '
                      'from: "$http_referer" ua: "$http_user_agent"';

    access_log  /var/www/access.log  main;

    server {
        listen   80;
        # 影响 Content-Type
        charset  utf-8;

        location / {
            root  /var/www/imgs;

            autoindex             on;
            autoindex_exact_size  off;
            autoindex_localtime   on;
        }

        location ~ .*\.(bmp|gif|ico|jpeg|jpg|png)$ {
            root     /var/www/imgs;
            expires  24h;
        }
    }
}
```

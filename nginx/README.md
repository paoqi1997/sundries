# Use Nginx

We need an HTTP Server!

## Install PCRE

Visit [www.pcre.org](http://www.pcre.org) to download package.

```
$ ./configure

$ make

$ sudo make install
```

## Install ZLib

Visit [zlib.net](http://zlib.net) to download package.

```
$ ./configure

$ make

$ sudo make install
```

## Install OpenSSL

As follows.

```
$ sudo apt-get install openssl

$ sudo apt-get install libssl-dev
```

## Install Nginx

Visit [nginx.org](http://nginx.org) to download package.

```
$ ./configure --with-http_ssl_module

$ make

$ sudo make install

$ sudo /usr/local/nginx/sbin/nginx
```

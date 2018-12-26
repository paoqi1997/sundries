# 简述

面向Linux的基本教程。

# 说明

以下操作均在elementary OS 5.0下调试通过。

# 常用命令

待续……

# 非apt/yum方式安装软件

有时候我们不得不这么做。

## Golang

首先提取相应的包。

```
$ sudo tar -C /usr/local -zxvf go1.10.7.linux-amd64.tar.gz
```

在$HOME/.profile文件中添加以下命令。

```
export PATH=$PATH:/usr/local/go/bin
```

运行一下。

```
$ source $HOME/.profile
```

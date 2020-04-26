# 简述

面向Git的基本教程。

# 说明

以下操作均在Git 2.17.1下调试通过。

# 基本操作

版本控制是非常有必要的。

## Config

配置一下。

```
$ git config --global user.name "paoqi1997"
$ git config --global user.email "604869221@qq.com"
```

## Work with GitHub

首先生成SSH Key，这里需要设置密码。

```
$ ssh-keygen -t rsa -C "604869221@qq.com"
```

将~/.ssh/id_rsa.pub文件中的内容添加到GitHub账户中，随后执行以下命令，这里会用到之前设置的密码。

```
$ ssh-add ~/.ssh/id_rsa
```

测试一下。

```
$ ssh -T git@github.com
```

以SSH方式从GitHub拉取pqnet项目到本地。

```
$ git clone git@github.com:paoqi1997/pqnet.git
```

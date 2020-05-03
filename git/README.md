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

查看配置。

```
$ git config -l
```

## Work with GitHub

首先生成SSH Key，如果需要的话，这里可以设置密码。

```
$ ssh-keygen -t rsa -C "604869221@qq.com"
```

将 ~/.ssh/id_rsa_github.pub 文件中的内容添加到 GitHub 账户中，随后执行以下命令。

```
# Could not open a connection to your authentication agent.
# 如果出现了以上错误，请执行以下命令以启动ssh-agent
$ ssh-agent bash

# 如果你之前生成SSH Key的时候设置了密码，那么这里会用到它
$ ssh-add ~/.ssh/id_rsa_github

# 查看代理中的私钥对应的公钥
$ ssh-add -L
# 查看代理中的私钥
$ ssh-add -l
```

测试一下。

```
$ ssh -T git@github.com

# Clone paoqi1997/pqnet with SSH
$ git clone git@github.com:paoqi1997/pqnet.git
```

## Learn Git

创建一个 Git 仓库。

```
$ mkdir learngit
$ cd learngit
$ git init

$ touch readme.txt
$ echo "Hello Git!" > readme.txt

$ git add readme.txt
$ git commit -m "create readme.txt"

# 查看提交历史
$ git log
# 查看提交历史（一行信息）
$ git log --oneline
```

查看difference。

```
$ echo "Git is better than SVN." >> readme.txt
$ git diff readme.txt
$ git status

$ git add readme.txt
$ git commit -m "update readme.txt"
```

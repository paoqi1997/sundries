# The manual of Git

面向Git的基本教程。

## 说明

以下操作均在 Git 2.17.1 下调试通过。

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
# 如果出现了以上错误，请执行以下命令以启动ssh-agent。
$ ssh-agent bash

# 如果你之前生成 SSH Key 的时候设置了密码，那么这里会用到它。
$ ssh-add ~/.ssh/id_rsa_github

# 查看代理中的私钥对应的公钥
$ ssh-add -L
# 查看代理中的私钥
$ ssh-add -l
```

测试一下。

```
$ ssh -T git@github.com

# Clone paoqi1997/enpa with SSH
$ git clone git@github.com:paoqi1997/enpa.git
```

如果嫌配置麻烦，可以直接通过 HTTPS 获取 repo。

```
# Clone paoqi1997/enpa with HTTPS
$ git clone https://github.com/paoqi1997/enpa.git
```

## Use proxy

这里是为了[免密登录](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%87%AD%E8%AF%81%E5%AD%98%E5%82%A8)。

```
# 这里将用户名中的'@'转义为%40
$ echo 'https://604869221%40qq.com:your-password@github.com.cnpmjs.org' > ~/.git-credentials

$ git config --global credential.helper store
```

测试一下。

```
$ git clone https://github.com.cnpmjs.org/paoqi1997/enpa.git
```

## Use GitHub CLI

获取 [GitHub CLI](https://cli.github.com) 并安装，随后进行身份验证，需要从[此处](https://github.com/settings/tokens)获取token。

```
$ gh auth login

$ gh auth status
```

执行以下命令。

```
# 查看repo
$ gh repo view godotengine/godot

# 获取repo
$ gh repo clone paoqi1997/enpa

$ cd enpa

# 查看issues
$ gh issue list
$ gh issue view 1
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

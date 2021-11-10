# Work with GitHub

## Add SSH Key

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

这里是为了[免密登录](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%87%AD%E8%AF%81%E5%AD%98%E5%82%A8)，稍后需要从[此处](https://github.com/settings/tokens)获取token。

```
# 这里将用户名中的'@'转义为%40
$ echo 'https://604869221%40qq.com:your-token@github.com.cnpmjs.org' > ~/.git-credentials

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

## Use GitHub Desktop

点击[这里](https://desktop.github.com)获取。

## Use GitHub for mobile

点击[这里](https://github.com/mobile)获取。

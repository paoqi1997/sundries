# Work with GitHub

## [Add SSH Key](https://docs.github.com/cn/authentication/connecting-to-github-with-ssh)

首先生成 SSH Key，如果需要的话，可以在这里设置密码。注意，RSA with SHA-1 已被废弃，详情请参考[该文](https://github.blog/2021-09-01-improving-git-protocol-security-github/)。

```
# 2022.1.11 后已废弃的方式
$ ssh-keygen -t rsa -C "604869221@qq.com"

# 目前使用的方式
$ ssh-keygen -t ed25519 -C "604869221@qq.com"
```

将 ~/.ssh/id_ed25519_github.pub 文件中的内容添加到 GitHub 账户中，随后执行以下命令。

```
# Could not open a connection to your authentication agent.
# 如果出现了以上错误，请执行以下命令以启动 ssh-agent。
$ ssh-agent bash

# 如果你之前生成 SSH Key 的时候设置了密码，那么这里会用到它。
$ ssh-add ~/.ssh/id_ed25519_github

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

如果嫌配置麻烦，可以直接通过 HTTPS 获取 repo。

```
# Clone paoqi1997/pqnet with HTTPS
$ git clone https://github.com/paoqi1997/pqnet.git
```

## [Use credentials](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%87%AD%E8%AF%81%E5%AD%98%E5%82%A8)

这里需要你从[此处](https://github.com/settings/tokens)获取 token。

```
# 这里将用户名（邮箱）中的'@'转义为%40
$ echo 'https://604869221%40qq.com:your-token@github.com' > ~/.git-credentials

$ git config --global credential.helper store
```

## Use proxy

启用 [FastGithub](https://github.com/dotnetcore/FastGithub)。

```
# https://github.com/dotnetcore/FastGithub/releases
$ wget https://github.com/dotnetcore/FastGithub/releases/download/2.1.4/fastgithub_linux-x64.zip

$ unzip -v fastgithub_linux-x64.zip
$ unzip fastgithub_linux-x64.zip

$ mv fastgithub_linux-x64 fastgithub
$ cd fastgithub

$ tmux new -s fastgithub
$ sudo ./fastgithub|tee what.cal

$ tmux attach -t fastgithub
$ tmux detach

$ tmux ls
$ tmux kill-session -t fastgithub

$ git config --global http.proxy http://127.0.0.1:38457
$ git config --get http.proxy
```

测试一下。

```
$ git clone https://github.com/paoqi1997/pqnet.git
```

## [GitHub CLI](https://cli.github.com)

进行身份验证时，需要使用从[此处](https://github.com/settings/tokens)获取的 token。

```
# Authenticate with a GitHub host.
$ gh auth login

# Verifies and displays information about your authentication state.
$ gh auth status
```

执行以下命令。

```
# 查看 repo
$ gh repo view godotengine/godot

# 获取 repo
$ gh repo clone paoqi1997/pqnet

$ cd pqnet
# 查看 issues
$ gh issue list
$ gh issue view 1
```

## [GitHub for mobile](https://github.com/mobile)

实际上 GitHub 官方会让你去 [Google Play](https://play.google.com/store/apps/details?id=com.github.android) 获取 APK，但你需要登录你的 Google 账户。一个比较好的办法是，你可以直接前往 [APK Downloader](https://apps.evozi.com/apk-downloader/?id=com.github.android) 下载 APK，从而免去登录 Google 账户的麻烦。

## TPs

### 官网

1. [GitHub Desktop](https://desktop.github.com)

2. [GitHub Status](https://www.githubstatus.com)

3. [GitHub Gist](https://gist.github.com)

### repos on GitHub

1. [cli/cli](https://github.com/cli/cli)

2. [desktop/desktop](https://github.com/desktop/desktop)

3. [github/docs](https://github.com/github/docs)

4. [github/hub](https://github.com/github/hub)

5. [github/linguist](https://github.com/github/linguist)

### more

1. [GitHub中文社区](https://www.githubs.cn)
